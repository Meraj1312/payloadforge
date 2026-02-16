import random
from typing import List


def case_variation(payloads: List[str]) -> List[str]:
    """
    Randomly change character casing.
    """
    mutated = []
    for payload in payloads:
        new_payload = ""
        for char in payload:
            if char.isalpha():
                new_payload += random.choice([char.upper(), char.lower()])
            else:
                new_payload += char
        mutated.append(new_payload)
    return mutated


def extra_whitespace(payloads: List[str]) -> List[str]:
    """
    Replace single spaces with multiple spaces.
    """
    return [p.replace(" ", "   ") for p in payloads]


def random_tabs(payloads: List[str]) -> List[str]:
    """
    Randomly insert tabs between words.
    """
    mutated = []
    for p in payloads:
        parts = p.split(" ")
        mutated.append("\t".join(parts))
    return mutated


def apply_all(payloads: List[str]) -> List[str]:
    """
    Apply all generic obfuscation techniques.
    """
    payloads = case_variation(payloads)
    payloads = extra_whitespace(payloads)
    payloads = random_tabs(payloads)
    return payloads
