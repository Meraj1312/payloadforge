import random


def case_variation(payload: str) -> str:
    """
    Randomly change character casing.
    """
    new_payload = ""
    for char in payload:
        if char.isalpha():
            new_payload += random.choice([char.upper(), char.lower()])
        else:
            new_payload += char
    return new_payload


def extra_whitespace(payload: str) -> str:
    """
    Replace single spaces with multiple spaces.
    """
    return payload.replace(" ", "   ")


def random_tabs(payload: str) -> str:
    """
    Replace spaces with tabs.
    """
    return "\t".join(payload.split(" "))


def apply_all(payload: str, mode: str | None = None) -> str:
    """
    Apply selected generic obfuscation technique.
    """

    if mode == "case":
        return case_variation(payload)

    elif mode == "whitespace":
        return extra_whitespace(payload)

    elif mode == "tabs":
        return random_tabs(payload)

    elif mode == "all":
        payload = case_variation(payload)
        payload = extra_whitespace(payload)
        payload = random_tabs(payload)
        return payload

    return payload
