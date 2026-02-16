# modules/sqli/sqli_obfuscation.py

import re
from typing import List

def insert_comments(payload: str) -> str:
    """
    Insert inline comment patterns inside SQL keywords.
    Example: UNION -> UN/**/ION
    """
    keywords = ["UNION", "SELECT", "WHERE", "AND", "OR", "FROM"]
    obf = payload
    for kw in keywords:
        # use case-insensitive replace by regex
        mid = len(kw) // 2
        new_kw = kw[:mid] + "/**/" + kw[mid:]
        obf = re.sub(kw, new_kw, obf, flags=re.IGNORECASE)
    return obf

def abuse_whitespace(payload: str) -> str:
    """
    Add extra spaces/tabs but keep result as a single string.
    This is SQL-specific spacing patterns (conservative).
    """
    # replace sequences with multiple spaces and add spaces around = and quotes
    p = re.sub(r'\s+', '    ', payload)
    p = p.replace("=", " = ").replace("'", " ' ")
    return p

def mixed_encoding(payload: str, url_encode_fn, base64_encode_fn) -> str:
    """
    Example of mixed encoding: url_encode then base64.
    We accept encoder functions (from global encoders) to avoid local duplication.
    """
    url_enc = url_encode_fn(payload)
    return base64_encode_fn(url_enc)

def obfuscate_variants(payload: str, url_encode_fn=None, base64_encode_fn=None) -> dict:
    """
    Return a dict of SQL-specific obfuscation variants (does not alter pipeline).
    Use these variants for demonstration or exporting.
    """
    variants = {
        "comment": insert_comments(payload),
        "whitespace": abuse_whitespace(payload)
    }
    if url_encode_fn and base64_encode_fn:
        variants["mixed"] = mixed_encoding(payload, url_encode_fn, base64_encode_fn)
    return variants

def obfuscate_list(payloads: List[str], url_encode_fn=None, base64_encode_fn=None) -> List[dict]:
    """
    Return list of dicts {payload: original, variants: {...}} for export/demos.
    This helper is for reporting, not the module's generate() output.
    """
    out = []
    for p in payloads:
        out.append({
            "payload": p,
            "variants": obfuscate_variants(p, url_encode_fn, base64_encode_fn)
        })
    return out
