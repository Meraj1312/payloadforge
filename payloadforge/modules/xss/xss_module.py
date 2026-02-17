#!/usr/bin/env python3
from typing import Dict, List
from ...core.base import BaseModule
from .xss_payloads import XSSPayloads
from .xss_obfuscation import XSSObfuscation
from .xss_signatures import XSSSignatures


class XSSModule(BaseModule):
    """
    XSS Payload Generation Module
    Generates XSS payloads based on context and applies optional obfuscation.
    """

    name = "xss"
    description = "Cross-Site Scripting (XSS) payload generator"

    def __init__(self):
        self.payloads = XSSPayloads()
        self.obfuscation = XSSObfuscation()
        self.signatures = XSSSignatures()

    def generate(self, context: str = "all", obfuscate: bool = False) -> Dict:
        """
        Generate XSS payloads.
        """

        payload_catalog = {
            "metadata": {
                "module": self.name,
                "context": context,
                "obfuscation": obfuscate
            },
            "payloads": []
        }

        # Get payloads
        if context == "all":
            payloads = self.payloads.get_all_payloads()
        else:
            payloads = self.payloads.get_payloads_by_context(context)

        for payload in payloads:

            payload_entry = {
                "payload": payload["payload"],
                "description": payload.get("description", ""),
                "bypass_techniques": payload.get("bypass_techniques", []),
                "defense_notes": self.signatures.get_defense_notes(payload["payload"])
            }

            if obfuscate:
                payload_entry["obfuscated_version"] = self.obfuscation.obfuscate(
                    payload["payload"]
                )

            payload_catalog["payloads"].append(payload_entry)

        return payload_catalog
