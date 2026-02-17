"""
Command Injection Detection Signatures and Defense Analysis
Educational module explaining detection methods and defensive strategies

Author: Security Research Team
Purpose: Help defenders understand attack patterns and implement proper defenses
"""

import re

# ==================== FILTER SIGNATURES ====================

COMMON_BLACKLISTS = {
    'commands': {
        'description': 'Commonly blacklisted commands',
        'patterns': [
            'whoami', 'id', 'cat', 'ls', 'dir', 'ping', 'curl', 'wget',
            'nc', 'netcat', 'bash', 'sh', 'cmd', 'powershell', 'eval',
            'exec', 'system', 'passthru', 'shell_exec', 'chmod', 'chown'
        ],
        'weakness': 'Easy to bypass with encoding, obfuscation, or wildcards'
    },
    'separators': {
        'description': 'Command separator metacharacters',
        'patterns': [';', '&&', '||', '|', '&', '\n', '`', '$()'],
        'weakness': 'Brace expansion and redirection bypass these'
    },
    'paths': {
        'description': 'Sensitive file paths',
        'patterns': [
            '/etc/passwd', '/etc/shadow', '/root/', '~/.ssh/',
            'C:\\Windows', 'C:\\Users', '/var/www', '/var/log'
        ],
        'weakness': 'Wildcard obfuscation easily bypasses exact matches'
    },
    'special_chars': {
        'description': 'Shell metacharacters',
        'patterns': ['<', '>', '{', '}', '(', ')', '[', ']', '*', '?', '$', '\\'],
        'weakness': 'Encoding and quote injection bypass'
    },
    'keywords': {
        'description': 'Dangerous keywords',
        'patterns': ['exec', 'eval', 'system', 'shell', 'spawn', 'run'],
        'weakness': 'Quote injection and character escaping bypass'
    }
}

# ==================== DETECTION REGEX PATTERNS ====================

DETECTION_PATTERNS = {
    'basic_separators': {
        'regex': r'[;&|`$<>]',
        'description': 'Detects basic command separators',
        'effectiveness': 'Low - easily bypassed',
        'bypassed_by': ['Encoding', 'Brace expansion', 'Quote injection']
    },
    'command_substitution': {
        'regex': r'`[^`]+`|\$\([^)]+\)',
        'description': 'Detects command substitution patterns',
        'effectiveness': 'Medium',
        'bypassed_by': ['Encoding', 'Nested obfuscation']
    },
    'shell_metachar': {
        'regex': r'[<>{}()\[\]\\*?$]',
        'description': 'Detects shell metacharacters',
        'effectiveness': 'Medium',
        'bypassed_by': ['URL encoding', 'Quote injection']
    },
    'path_traversal': {
        'regex': r'\.\./|\.\.\\',
        'description': 'Detects path traversal attempts',
        'effectiveness': 'Low',
        'bypassed_by': ['Absolute paths', 'Wildcard obfuscation']
    },
    'sensitive_paths': {
        'regex': r'/etc/passwd|/etc/shadow|\.ssh|C:\\Windows',
        'description': 'Detects access to sensitive paths',
        'effectiveness': 'Low',
        'bypassed_by': ['Wildcards', 'Variable expansion']
    },
    'brace_expansion': {
        'regex': r'\{[^}]+,[^}]+\}',
        'description': 'Detects brace expansion patterns',
        'effectiveness': 'Medium-High',
        'bypassed_by': ['Nested braces', 'Variable obfuscation']
    },
    'encoding_patterns': {
        'regex': r'%[0-9a-fA-F]{2}|\\x[0-9a-fA-F]{2}|\\[0-7]{3}',
        'description': 'Detects encoded characters',
        'effectiveness': 'Medium',
        'bypassed_by': ['Double encoding', 'Mixed encoding']
    },
    'rev_command': {
        'regex': r'\brev\b|<<<',
        'description': 'Detects string reversal attempts',
        'effectiveness': 'Medium',
        'bypassed_by': ['Parameter-based reversal', 'Custom reversal functions']
    },
    'base64_decode': {
        'regex': r'base64\s+-d|base64\s+--decode',
        'description': 'Detects base64 decoding',
        'effectiveness': 'Medium',
        'bypassed_by': ['Custom decode functions', 'Alternative encoding']
    },
    'eval_patterns': {
        'regex': r'\beval\b|\bexec\b',
        'description': 'Detects eval/exec usage',
        'effectiveness': 'High',
        'bypassed_by': ['Variable indirection', 'Arithmetic expansion']
    }
}

# ==================== WAF EVASION ANALYSIS ====================

WAF_BYPASS_TECHNIQUES = {
    'url_encoding': {
        'description': 'URL encode special characters',
        'example': '; → %3B',
        'blocks': ['Basic string matching'],
        'detected_by': ['Decoding WAFs', 'Multi-stage analysis'],
        'success_rate': 'Medium (60%)',
        'modern_defense': 'Normalize and decode all inputs before checking'
    },
    'double_encoding': {
        'description': 'Apply URL encoding twice',
        'example': '; → %253B',
        'blocks': ['Single-decode filters'],
        'detected_by': ['Recursive decoding', 'Proper normalization'],
        'success_rate': 'Medium-High (70%)',
        'modern_defense': 'Decode recursively until stable'
    },
    'quote_injection': {
        'description': 'Break keywords with quotes',
        'example': "cat → c''at",
        'blocks': ['Exact keyword matching'],
        'detected_by': ['Shell AST parsing', 'Quote removal before check'],
        'success_rate': 'High (80%)',
        'modern_defense': 'Parse as shell would, then validate'
    },
    'case_variation': {
        'description': 'Mix case (Windows)',
        'example': 'whoami → WhOaMi',
        'blocks': ['Case-sensitive blacklists'],
        'detected_by': ['Case-insensitive matching'],
        'success_rate': 'Low-Medium (50%)',
        'modern_defense': 'Normalize to lowercase before checking'
    },
    'wildcard_obfuscation': {
        'description': 'Use wildcards in paths/commands',
        'example': '/etc/passwd → /e??/p*wd',
        'blocks': ['Exact path matching'],
        'detected_by': ['Glob expansion before check', 'Wildcard detection'],
        'success_rate': 'High (85%)',
        'modern_defense': 'Block wildcards or expand and validate'
    },
    'brace_expansion': {
        'description': 'No separators needed',
        'example': '{cat,/etc/passwd}',
        'blocks': ['Separator-based detection'],
        'detected_by': ['AST parsing', 'Brace pattern detection'],
        'success_rate': 'Very High (90%)',
        'modern_defense': 'Parse shell syntax, reject complex expansions'
    },
    'space_bypass': {
        'description': 'Replace spaces with IFS or redirects',
        'example': 'cat /etc → cat${IFS}/etc',
        'blocks': ['Space-dependent parsing'],
        'detected_by': ['Variable expansion awareness', 'IFS detection'],
        'success_rate': 'High (75%)',
        'modern_defense': 'Expand variables before validation'
    },
    'string_reversal': {
        'description': 'Reverse payload, use rev at runtime',
        'example': "cat → rev<<<'tac'",
        'blocks': ['Signature matching'],
        'detected_by': ['rev command detection', 'Pipeline analysis'],
        'success_rate': 'High (80%)',
        'modern_defense': 'Flag rev usage in user input contexts'
    },
    'arithmetic_expansion': {
        'description': 'Generate characters via arithmetic',
        'example': '$(printf "\\x63\\x61\\x74")',
        'blocks': ['Command blacklists'],
        'detected_by': ['Printf pattern detection', 'Arithmetic expansion limits'],
        'success_rate': 'Very High (90%)',
        'modern_defense': 'Restrict arithmetic expansion in user input'
    },
    'multi_layer': {
        'description': 'Chain multiple techniques',
        'example': 'Base64 + reversal + brace',
        'blocks': ['Single-layer detection'],
        'detected_by': ['Multi-stage analysis', 'Sandbox execution'],
        'success_rate': 'Extremely High (95%)',
        'modern_defense': 'Only runtime/sandbox analysis reliable'
    }
}

# ==================== MODERN DEFENSE MECHANISMS ====================

MODERN_DEFENSES = {
    'input_validation': {
        'description': 'Whitelist-based input validation',
        'implementation': [
            'Define allowed character set (alphanumeric + limited special)',
            'Reject any input containing disallowed characters',
            'Use strict regex patterns',
            'Validate length limits'
        ],
        'effectiveness': 'Very High',
        'example': r'^[a-zA-Z0-9._-]+$',
        'pros': 'Blocks most attacks at input level',
        'cons': 'May be too restrictive for some use cases'
    },
    'parameterized_commands': {
        'description': 'Use subprocess without shell',
        'implementation': [
            'subprocess.run(["command", arg1, arg2], shell=False)',
            'Never concatenate user input into command strings',
            'Pass arguments as list elements',
            'Avoid shell=True entirely'
        ],
        'effectiveness': 'Extremely High',
        'example': 'subprocess.run(["ping", "-c", "1", user_ip], shell=False)',
        'pros': 'Nearly eliminates command injection risk',
        'cons': 'Limited to simple command execution'
    },
    'sandboxing': {
        'description': 'Execute in restricted environment',
        'implementation': [
            'Use containers (Docker) with limited capabilities',
            'chroot jails',
            'seccomp filters',
            'Restricted shells (rbash)',
            'Drop privileges (setuid)'
        ],
        'effectiveness': 'High',
        'pros': 'Limits damage even if injection succeeds',
        'cons': 'Complex setup, performance overhead'
    },
    'ast_parsing': {
        'description': 'Parse input as shell would',
        'implementation': [
            'Use shell parser library',
            'Analyze AST for dangerous patterns',
            'Detect expansions, substitutions, redirects',
            'Reject complex syntax'
        ],
        'effectiveness': 'Very High',
        'pros': 'Understands shell semantics',
        'cons': 'Complex to implement, parser must match shell exactly'
    },
    'behavioral_analysis': {
        'description': 'Monitor execution behavior',
        'implementation': [
            'Log all command executions',
            'Monitor child process spawning',
            'Detect unusual process trees',
            'Track network connections from processes',
            'Anomaly detection for process behavior'
        ],
        'effectiveness': 'High',
        'pros': 'Detects successful attacks',
        'cons': 'Reactive, not preventive'
    },
    'least_privilege': {
        'description': 'Run with minimal necessary permissions',
        'implementation': [
            'Dedicated service accounts',
            'No root/admin privileges',
            'Read-only filesystems where possible',
            'Network segmentation',
            'Capability-based restrictions'
        ],
        'effectiveness': 'Medium-High',
        'pros': 'Reduces attack impact',
        'cons': "Doesn't prevent injection"
    }
}

# ==================== DETECTION FUNCTIONS ====================

def analyze_payload(payload):
    """
    Analyze a payload for dangerous patterns
    
    Args:
        payload (str): The command injection payload to analyze
    
    Returns:
        dict: Analysis results with detections and risk assessment
    """
    findings = {
        'dangerous_chars': [],
        'suspicious_commands': [],
        'detected_patterns': [],
        'bypass_techniques': [],
        'risk_level': 'low',
        'detection_probability': 'high'
    }
    
    # Check for dangerous characters
    dangerous = [';', '&', '|', '`', '$', '<', '>', '{', '}', '(', ')', '*', '?']
    for char in dangerous:
        if char in payload:
            findings['dangerous_chars'].append(char)
    
    # Check for commands
    for cmd in COMMON_BLACKLISTS['commands']['patterns']:
        if cmd in payload.lower():
            findings['suspicious_commands'].append(cmd)
    
    # Check detection patterns
    for pattern_name, pattern_info in DETECTION_PATTERNS.items():
        if re.search(pattern_info['regex'], payload):
            findings['detected_patterns'].append({
                'pattern': pattern_name,
                'description': pattern_info['description'],
                'effectiveness': pattern_info['effectiveness']
            })
    
    # Identify bypass techniques
    if '%' in payload and re.search(r'%[0-9a-fA-F]{2}', payload):
        findings['bypass_techniques'].append('URL encoding')
    if re.search(r"['\"]", payload) and len(re.findall(r"['\"]", payload)) > 2:
        findings['bypass_techniques'].append('Quote injection')
    if '${IFS}' in payload or '$IFS' in payload:
        findings['bypass_techniques'].append('IFS space bypass')
    if re.search(r'\{[^}]+,[^}]+\}', payload):
        findings['bypass_techniques'].append('Brace expansion')
    if 'rev' in payload or '<<<' in payload:
        findings['bypass_techniques'].append('String reversal')
    if 'base64' in payload:
        findings['bypass_techniques'].append('Base64 encoding')
    if re.search(r'\\x[0-9a-fA-F]{2}', payload):
        findings['bypass_techniques'].append('Hex encoding')
    
    # Calculate risk level
    risk_score = 0
    risk_score += len(findings['dangerous_chars']) * 2
    risk_score += len(findings['suspicious_commands']) * 5
    risk_score += len(findings['bypass_techniques']) * 3
    
    if risk_score >= 20:
        findings['risk_level'] = 'critical'
        findings['detection_probability'] = 'medium'
    elif risk_score >= 10:
        findings['risk_level'] = 'high'
        findings['detection_probability'] = 'medium-high'
    elif risk_score >= 5:
        findings['risk_level'] = 'medium'
        findings['detection_probability'] = 'high'
    else:
        findings['risk_level'] = 'low'
        findings['detection_probability'] = 'very high'
    
    # Advanced evasion techniques lower detection
    if len(findings['bypass_techniques']) >= 2:
        findings['detection_probability'] = 'low'
    
    return findings

def explain_detection(payload):
    """
    Explain why a payload would or wouldn't be detected
    
    Args:
        payload (str): Command injection payload
    
    Returns:
        dict: Detailed explanation of detection/evasion
    """
    analysis = analyze_payload(payload)
    
    explanation = {
        'payload': payload,
        'analysis': analysis,
        'detection_methods': [],
        'evasion_success': [],
        'recommendations': []
    }
    
    # What would detect it
    if analysis['dangerous_chars']:
        explanation['detection_methods'].append({
            'method': 'Character blacklist',
            'detects': f"Dangerous characters: {', '.join(analysis['dangerous_chars'])}",
            'reliability': 'Medium'
        })
    
    if analysis['suspicious_commands']:
        explanation['detection_methods'].append({
            'method': 'Command blacklist',
            'detects': f"Suspicious commands: {', '.join(analysis['suspicious_commands'])}",
            'reliability': 'Low - easily bypassed'
        })
    
    for pattern in analysis['detected_patterns']:
        explanation['detection_methods'].append({
            'method': f"Pattern matching ({pattern['pattern']})",
            'detects': pattern['description'],
            'reliability': pattern['effectiveness']
        })
    
    # What evasion techniques work
    for technique in analysis['bypass_techniques']:
        if technique in WAF_BYPASS_TECHNIQUES:
            info = WAF_BYPASS_TECHNIQUES[technique]
            explanation['evasion_success'].append({
                'technique': technique,
                'success_rate': info['success_rate'],
                'bypasses': info['blocks']
            })
    
    # Defensive recommendations
    explanation['recommendations'] = [
        'Use parameterized commands (subprocess without shell)',
        'Implement strict whitelist validation',
        'Parse input as shell AST before processing',
        'Apply principle of least privilege',
        'Monitor process execution for anomalies'
    ]
    
    if 'brace expansion' in analysis['bypass_techniques']:
        explanation['recommendations'].append('Block or parse brace expansion syntax')
    
    if 'encoding' in ' '.join(analysis['bypass_techniques']).lower():
        explanation['recommendations'].append('Normalize input (decode recursively)')
    
    return explanation

def get_defense_recommendation(attack_type):
    """
    Get specific defense recommendations for attack type
    
    Args:
        attack_type (str): Type of attack (separator, encoding, obfuscation, etc.)
    
    Returns:
        dict: Defense recommendations
    """
    defenses = {
        'separator': {
            'primary': 'parameterized_commands',
            'secondary': ['input_validation', 'sandboxing'],
            'explanation': 'Separators are the core mechanism. Best defense: no shell.'
        },
        'encoding': {
            'primary': 'input_validation',
            'secondary': ['ast_parsing', 'behavioral_analysis'],
            'explanation': 'Decode and normalize input before validation.'
        },
        'obfuscation': {
            'primary': 'ast_parsing',
            'secondary': ['sandboxing', 'behavioral_analysis'],
            'explanation': 'Obfuscation requires semantic understanding. Parse as shell would.'
        },
        'advanced': {
            'primary': 'sandboxing',
            'secondary': ['behavioral_analysis', 'least_privilege'],
            'explanation': 'Advanced techniques bypass static analysis. Limit damage via isolation.'
        }
    }
    
    return defenses.get(attack_type, defenses['separator'])

# ==================== EDUCATIONAL SUMMARY ====================

DEFENSE_SUMMARY = """
COMMAND INJECTION DEFENSE - KEY PRINCIPLES

1. PREVENTION (Best Approach):
   - NEVER use shell=True with user input
   - Use subprocess with argument lists
   - Example: subprocess.run(["ping", user_ip], shell=False)

2. INPUT VALIDATION (If shell is unavoidable):
   - Whitelist allowed characters: ^[a-zA-Z0-9._-]+$
   - Reject everything else
   - No blacklists - they're incomplete

3. NORMALIZATION:
   - Decode URL encoding (recursively)
   - Expand variables before checking
   - Remove quotes and parse as shell would

4. SANDBOXING:
   - Run commands in restricted environment
   - Drop privileges
   - Use containers/chroot

5. MONITORING:
   - Log all command executions
   - Alert on unusual process spawning
   - Monitor for known attack patterns

6. DEFENSE IN DEPTH:
   - Combine multiple techniques
   - No single defense is perfect
   - Layer prevention + detection + response

WHY BLACKLISTS FAIL:
- Infinite bypass variations exist
- Encoding (URL, Base64, Hex)
- Obfuscation (quotes, wildcards, variables)
- Shell features (brace expansion, redirection)
- New techniques constantly discovered

MODERN ATTACKS BYPASS:
- String matching (encoding)
- Character filters (quote injection)
- Separator detection (brace expansion)
- Signature matching (reversal, arithmetic)
- Static analysis (runtime construction)

ONLY RELIABLE DEFENSES:
1. Don't use shell
2. If you must, strict whitelist validation
3. Sandbox everything
4. Monitor execution behavior
"""

if __name__ == '__main__':
    print("=" * 70)
    print("COMMAND INJECTION DEFENSE SIGNATURES MODULE")
    print("=" * 70)
    
    # Test payload analysis
    test_payloads = [
        "; whoami",
        "{cat,/etc/passwd}",
        "rev<<<'tac'",
        "$(printf \"\\x63\\x61\\x74\")"
    ]
    
    for payload in test_payloads:
        print(f"\n[ANALYSIS] Payload: {payload}")
        analysis = analyze_payload(payload)
        print(f"Risk Level: {analysis['risk_level'].upper()}")
        print(f"Detection Probability: {analysis['detection_probability']}")
        print(f"Bypass Techniques: {', '.join(analysis['bypass_techniques']) if analysis['bypass_techniques'] else 'None detected'}")
    
    print("\n" + "=" * 70)
    print(DEFENSE_SUMMARY)
