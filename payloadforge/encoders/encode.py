from __future__ import annotations

import base64
from urllib.parse import quote


def apply_encoding(value: str, mode: str) -> str:
    if mode == "none":
        return value
    if mode == "url":
        return quote(value, safe="")
    if mode == "base64":
        return base64.b64encode(value.encode("utf-8")).decode("ascii")
    if mode == "hex":
        return value.encode("utf-8").hex()
    raise ValueError(f"Unsupported encode mode: {mode}")
