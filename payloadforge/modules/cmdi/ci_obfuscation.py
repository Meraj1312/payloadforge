"""
Command Injection Obfuscation
Educational transformations only
"""

import base64
import urllib.parse


class CMDIObfuscation:

    def obfuscate(self, payload: str, technique: str) -> str:

        if technique == "url":
            return urllib.parse.quote(payload)

        if technique == "base64":
            encoded = base64.b64encode(payload.encode()).decode()
            return f"echo {encoded} | base64 -d"

        if technique == "ifs":
            return payload.replace(" ", "${IFS}")

        if technique == "hex":
            return ''.join(f"\\x{ord(c):02x}" for c in payload)

        return payload
