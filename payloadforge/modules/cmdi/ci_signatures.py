"""
Command Injection Detection Signatures
"""

from typing import Dict


COMMON_SEPARATORS = [";", "&&", "||", "|", "`", "$("]
COMMON_COMMANDS = ["whoami", "id", "cat", "ls", "ping", "curl", "wget"]


def analyze_payload(payload: str) -> Dict:

    findings = {
        "dangerous_tokens": [],
        "risk_level": "low"
    }

    for sep in COMMON_SEPARATORS:
        if sep in payload:
            findings["dangerous_tokens"].append(sep)

    for cmd in COMMON_COMMANDS:
        if cmd in payload.lower():
            findings["dangerous_tokens"].append(cmd)

    score = len(findings["dangerous_tokens"])

    if score >= 4:
        findings["risk_level"] = "high"
    elif score >= 2:
        findings["risk_level"] = "medium"

    return findings
