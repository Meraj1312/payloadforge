"""
Security Control Simulation
Educational WAF / filter behavior simulation
"""

def simulate(payload: str) -> dict:
    """
    Simulates basic defensive filtering logic.
    Educational only.
    """

    blocked_patterns = [
        "<script",
        "javascript:",
        "eval(",
        ";",
        "&&",
        "|",
        "`",
        "$(",
        "union select",
        "or 1=1",
    ]

    detected = []

    for pattern in blocked_patterns:
        if pattern.lower() in payload.lower():
            detected.append(pattern)

    if detected:
        return {
            "blocked": True,
            "detected_patterns": detected,
            "risk_level": "high",
            "reason": "Matched known dangerous signatures"
        }

    return {
        "blocked": False,
        "detected_patterns": [],
        "risk_level": "low",
        "reason": "No obvious signature match"
    }
