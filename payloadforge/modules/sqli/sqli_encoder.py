# sqli_encoder.py

import base64
import urllib.parse

class SQLiEncoder:
    @staticmethod
    def url_encode(payload: str) -> str:
        return urllib.parse.quote(payload)

    @staticmethod
    def base64_encode(payload: str) -> str:
        return base64.b64encode(payload.encode()).decode()

    @staticmethod
    def hex_encode(payload: str) -> str:
        # return space-separated hex representation
        return ' '.join(hex(ord(c))[2:] for c in payload)

    @staticmethod
    def encode_all(payloads: list, encode_type: str) -> list:
        """Apply encoding to each payload in the list (list of dicts with 'payload' key)."""
        for item in payloads:
            if encode_type == "url":
                item["encoded"] = SQLiEncoder.url_encode(item["payload"])
            elif encode_type == "base64":
                item["encoded"] = SQLiEncoder.base64_encode(item["payload"])
            elif encode_type == "hex":
                item["encoded"] = SQLiEncoder.hex_encode(item["payload"])
        return payloads