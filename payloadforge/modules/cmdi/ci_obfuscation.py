"""
Command Injection Obfuscation Module
"""

import base64
import urllib.parse
import binascii


class CommandObfuscator:

    @staticmethod
    def url_encode(payload):
        return urllib.parse.quote(payload)

    @staticmethod
    def base64_encode(payload):
        return base64.b64encode(payload.encode()).decode()

    @staticmethod
    def hex_encode(payload):
        return binascii.hexlify(payload.encode()).decode()

    @staticmethod
    def ifs_bypass(payload):
        return payload.replace(" ", "${IFS}")

    @staticmethod
    def quote_injection(payload):
        return payload.replace("a", "a''")

    @staticmethod
    def wildcard_obfuscation(payload):
        return payload.replace("etc", "e??")


OBFUSCATION_PRESETS = {
    'light': ['url_encode'],
    'medium': ['quote_injection', 'ifs_bypass'],
    'heavy': ['wildcard_obfuscation', 'base64_encode']
}
