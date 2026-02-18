"""
Command Injection Detection Signatures and Defense Analysis
"""

import re


COMMON_BLACKLISTS = {
    'commands': [
        'whoami', 'id', 'cat', 'ls', 'dir', 'ping', 'curl',
        'wget', 'nc', 'bash', 'sh', 'cmd', 'powershell'
    ],
    'separators': [';', '&&', '||', '|', '&', '\n', '`', '$()']
}


def analyze_payload(payload):
    findings = {
        'dangerous_chars': [],
        'suspicious_commands': [],
        'risk_level': 'low'
    }

    for char in COMMON_BLACKLISTS['separators']:
        if char in payload:
            findings['dangerous_chars'].append(char)

    for cmd in COMMON_BLACKLISTS['commands']:
        if cmd in payload.lower():
            findings['suspicious_commands'].append(cmd)

    score = len(findings['dangerous_chars']) * 2 + len(findings['suspicious_commands']) * 5

    if score >= 10:
        findings['risk_level'] = 'high'
    elif score >= 5:
        findings['risk_level'] = 'medium'

    return findings
