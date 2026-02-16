import re
from typing import List, Dict


BLACKLIST_PATTERNS = [
    r"<script>",
    r"UNION",
    r"SELECT",
    r"&&",
    r";",
]


def simulate(payloads: List[str]) -> List[Dict]:
    """
    Simulate basic security controls (blacklist filtering).
    Returns structured results.
    """
    results = []

    for payload in payloads:
        blocked = False
        reason = None

        for pattern in BLACKLIST_PATTERNS:
            if re.search(pattern, payload, re.IGNORECASE):
                blocked = True
                reason = f"Blocked by pattern: {pattern}"
                break

        results.append({
            "payload": payload,
            "blocked": blocked,
            "reason": reason if blocked else "Passed filters"
        })

    return results
