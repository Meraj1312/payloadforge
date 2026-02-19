from typing import List, Dict
from payloadforge.core.base import BaseModule
from .xss_payloads import XSSPayloads


class XSSModule(BaseModule):
    """
    XSS Payload Generation Module
    Returns standardized payload structure compatible with PayloadForge pipeline.
    """

    name = "xss"

    def __init__(self):
        self.payloads = XSSPayloads()

    def generate(self, context: str = "all", payload_type: str = "all", **kwargs) -> List[Dict]:
        """
        Generate structured XSS payloads.
        Returns List[dict] to match framework contract.
        """

        contexts = ["html", "attribute", "javascript"] if context == "all" else [context]
        types = ["reflected", "stored", "dom"] if payload_type == "all" else [payload_type]

        results: List[Dict] = []

        for ctx in contexts:
            for ptype in types:

                if ptype == "reflected":
                    payloads = self.payloads.get_reflected(ctx)

                elif ptype == "stored":
                    payloads = self.payloads.get_stored(ctx)

                elif ptype == "dom":
                    payloads = self.payloads.get_dom_based(ctx)

                else:
                    continue

                for item in payloads:
                    results.append({
                        "payload": item["payload"],
                        "type": f"{ptype}_{ctx}",
                        "database": None,
                        "os": None
                    })

        return results
