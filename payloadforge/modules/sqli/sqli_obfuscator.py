# sqli_obfuscator.py

import random
import re

class SQLiObfuscator:
    @staticmethod
    def insert_comments(payload: str) -> str:
        """Insert inline comments in SQL keywords."""
        keywords = ["UNION", "SELECT", "WHERE", "AND", "OR", "FROM"]
        obf = payload
        for kw in keywords:
            if kw in obf.upper():
                mid = len(kw) // 2
                new_kw = kw[:mid] + "/**/" + kw[mid:]
                obf = re.sub(kw, new_kw, obf, flags=re.IGNORECASE)
        return obf

    @staticmethod
    def abuse_whitespace(payload: str) -> str:
        """Add some extra spaces, but not too many."""
        # Replace any whitespace sequence with two spaces
        payload = re.sub(r'\s+', '    ', payload)
        # Add spaces around operators
        payload = payload.replace("=", " = ").replace("'", " ' ")
        return payload

    @staticmethod
    def mixed_encoding(payload: str) -> str:
        """First URL encode, then base64."""
        from sqli_encoder import SQLiEncoder
        url_enc = SQLiEncoder.url_encode(payload)
        return SQLiEncoder.base64_encode(url_enc)

   
        result = payload
        for kw, mixed in mapping.items():
            result = re.sub(kw, mixed, result, flags=re.IGNORECASE)
        return result

    @staticmethod
    def obfuscate_all(payloads: list) -> list:
        """Apply all obfuscation techniques to each payload."""
        for item in payloads:
            orig = item["payload"]
            item["obfuscated"] = {
                "comment": SQLiObfuscator.insert_comments(orig),
                "whitespace": SQLiObfuscator.abuse_whitespace(orig),
                "mixed": SQLiObfuscator.mixed_encoding(orig),
            }
        return payloads