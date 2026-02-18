"""
Command Injection Obfuscation Module
Standard encoding and evasion techniques for educational purposes
"""

import base64
import urllib.parse
import binascii

class CommandObfuscator:
    """
    Standard obfuscation techniques for command injection payloads
    """
    # ... (keep all methods exactly as Ali wrote them)

# Obfuscation presets
OBFUSCATION_PRESETS = {
    'light': { 'techniques': ['url'], 'description': 'Light obfuscation - URL encoding only', 'evasion_level': 'Low' },
    'medium': { 'techniques': ['quote', 'ifs'], 'description': 'Medium obfuscation', 'evasion_level': 'Medium' },
    'heavy': { 'techniques': ['variable', 'wildcard', 'base64'], 'description': 'Heavy obfuscation', 'evasion_level': 'High' },
    'extreme': { 'techniques': ['backslash', 'variable', 'wildcard', 'base64'], 'description': 'Extreme evasion', 'evasion_level': 'Very High' }
}

def get_preset(preset_name):
    return OBFUSCATION_PRESETS.get(preset_name, OBFUSCATION_PRESETS['light'])
