"""
PayloadForge Exporter Module
Handles formatting and exporting generated payload data.
"""

import json
from pathlib import Path
from datetime import datetime


class Exporter:
    """
    Handles exporting payload data into different formats.
    """

    def __init__(self, output_format: str = "terminal", filename: str | None = None):
        self.output_format = output_format
        self.filename = filename
        self.export_dir = Path("payloadforge/data/sample_exports")
        self.export_dir.mkdir(parents=True, exist_ok=True)

    def export(self, payloads: list[dict]):
        """
        Main export dispatcher.
        """
        if self.output_format == "terminal":
            self._export_terminal(payloads)
        elif self.output_format == "json":
            self._export_json(payloads)
        elif self.output_format == "txt":
            self._export_txt(payloads)
        elif self.output_format == "burp":
            self._export_burp(payloads)
        elif self.output_format == "zap":
            self._export_zap(payloads)
        elif self.output_format == "all":
            self._export_terminal(payloads)
            self._export_json(payloads)
            self._export_txt(payloads)
        else:
            raise ValueError(f"Unsupported output format: {self.output_format}")

    # ========================
    # TERMINAL OUTPUT
    # ========================

    def _export_terminal(self, payloads: list[dict]):
        for item in payloads:
            print("=" * 60)
            print(f"[ID] {item.get('id')}")
            print(f"[Payload] {item.get('payload')}")
            print(f"[Category] {item.get('type')}")
            print(f"[Target] {item.get('database') or item.get('os')}")
            if "defense" in item:
                print(f"[Defense Info] {item['defense']}")
        print("=" * 60)

    # ========================
    # JSON OUTPUT
    # ========================

    def _export_json(self, payloads: list[dict]):
        filename = self._get_filename("json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(payloads, f, indent=4)
        print(f"[+] JSON exported to {filename}")

    # ========================
    # TXT OUTPUT
    # ========================

    def _export_txt(self, payloads: list[dict]):
        filename = self._get_filename("txt")
        with open(filename, "w", encoding="utf-8") as f:
            for item in payloads:
                f.write(f"{item.get('payload')}\n")
        print(f"[+] TXT exported to {filename}")

    # ========================
    # BURP FORMAT
    # ========================

    def _export_burp(self, payloads: list[dict]):
        filename = self._get_filename("txt", suffix="_burp")
        with open(filename, "w", encoding="utf-8") as f:
            for item in payloads:
                f.write(item.get("payload") + "\n")
        print(f"[+] Burp-ready payload list saved to {filename}")

    # ========================
    # ZAP FORMAT
    # ========================

    def _export_zap(self, payloads: list[dict]):
        filename = self._get_filename("txt", suffix="_zap")
        with open(filename, "w", encoding="utf-8") as f:
            for item in payloads:
                f.write(item.get("payload") + "\n")
        print(f"[+] ZAP-ready payload list saved to {filename}")

    # ========================
    # INTERNAL
    # ========================

    def _get_filename(self, extension: str, suffix: str = ""):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = self.filename or f"payloadforge_{timestamp}{suffix}"
        return self.export_dir / f"{name}.{extension}"
