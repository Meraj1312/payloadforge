"""
CMDI Module – PayloadForge Integration
Educational templates only
"""

from typing import List, Dict

from payloadforge.modules.cmdi.cmdi_payloads import CMDIPayloads
from payloadforge.modules.cmdi.cmdi_obfuscation import CMDIObfuscation
from payloadforge.modules.cmdi.cmdi_signatures import analyze_payload


class CMDIModule:

    def __init__(self):
        self.payloads = CMDIPayloads()
        self.obfuscation = CMDIObfuscation()

    def generate(self, category: str = "all", **kwargs) -> List[Dict]:

        if category == "basic":
            base_payloads = self.payloads.get_basic()
        elif category == "blind":
            base_payloads = self.payloads.get_blind()
        elif category == "filter_bypass":
            base_payloads = self.payloads.get_filter_bypass()
        else:
            base_payloads = self.payloads.get_all()

        results: List[Dict] = []

        for item in base_payloads:

            payload = item["payload"]

            entry = {
                "payload": payload,
                "type": f"cmdi_{item.get('context')}",
                "database": None,
                "os": "linux",
            }

            # Module-specific obfuscation
            entry["module_obfuscation"] = {
                "url": self.obfuscation.obfuscate(payload, "url"),
                "base64": self.obfuscation.obfuscate(payload, "base64"),
                "ifs": self.obfuscation.obfuscate(payload, "ifs"),
                "hex": self.obfuscation.obfuscate(payload, "hex"),
            }

            entry["analysis"] = analyze_payload(payload)

            results.append(entry)

        return results
