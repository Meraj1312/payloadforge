"""
PayloadForge - Educational Payload Generation Framework
Main Controller

This file acts as the CLI entry point.
It coordinates:
- Module selection
- Payload generation
- Encoding
- Obfuscation
- Security control simulation
- Exporting
"""

from __future__ import annotations

import argparse
import sys

# Core
from payloadforge.core.exporter import Exporter
from payloadforge.core.generic_obfuscation import apply_all
from payloadforge.core.security_controls import simulate

# Encoder
from payloadforge.encoders.encode import apply_encoding

# Modules
from payloadforge.modules.sqli.sqli_module import SQLIModule
from payloadforge.modules.xss.xss_module import XSSModule
from payloadforge.modules.cmdi.cmdi_module import CMDIModule

# Banner dependencies
import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama for Windows
init(autoreset=True)


def show_banner():
    """Display the tool banner (once at startup)."""
    banner = pyfiglet.figlet_format("PayloadForge", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "Educational Payload Generation Framework")
    print(Fore.GREEN + "Version: 1.0.0")
    print(Fore.CYAN + "=" * 65 + Style.RESET_ALL)


def get_module(module_name: str):
    """Returns the correct module instance."""
    module_map = {
        "sqli": SQLIModule,
        "xss": XSSModule,
        "cmdi": CMDIModule,
    }

    if module_name not in module_map:
        raise ValueError(f"Unsupported module: {module_name}")

    return module_map[module_name]()


def process_payloads(payloads: list[dict], args) -> list[dict]:
    """Applies encoding, obfuscation and defense simulation."""
    processed = []

    for idx, item in enumerate(payloads, start=1):
        payload_value = item.get("payload")

        if args.encode and args.encode != "none":
            payload_value = apply_encoding(payload_value, args.encode)

        if args.obfuscate:
            payload_value = apply_all(payload_value, args.obfuscate)

        defense_result = simulate(payload_value)

        processed.append(
            {
                "id": idx,
                "payload": payload_value,
                "type": item.get("type"),
                "database": item.get("database"),
                "os": item.get("os"),
                "defense": defense_result,
            }
        )

    return processed


def main():
    show_banner()  

    parser = argparse.ArgumentParser(
        description="PayloadForge - Educational Payload Generator"
    )

    # Core arguments
    parser.add_argument(
        "-m",
        "--module",
        required=True,
        choices=["sqli", "xss", "cmdi"],
        help="Select attack module",
    )

    parser.add_argument(
        "-e",
        "--encode",
        default="none",
        choices=["none", "url", "base64", "hex"],
        help="Encoding mode",
    )

    parser.add_argument(
        "-o",
        "--obfuscate",
        default=None,
        help="Obfuscation mode (currently supports: case)",
    )

    parser.add_argument(
        "-f",
        "--format",
        default="terminal",
        choices=["terminal", "json", "txt", "burp", "zap", "all"],
        help="Export format",
    )

    parser.add_argument(
        "--filename",
        default=None,
        help="Custom export filename (without extension)",
    )

    # SQLi-specific arguments
    parser.add_argument(
        "--db",
        default="all",
        choices=["all", "mysql", "postgresql", "mssql"],
        help="Select target database (SQLi only)",
    )

    parser.add_argument(
        "--type",
        dest="injection_type",
        default="all",
        choices=["all", "error", "union", "blind", "comment_bypass", "case_variation"],
        help="Select injection type (SQLi only)",
    )

    args = parser.parse_args()

    try:
        # 1️ Load module
        module = get_module(args.module)

        # 2️ Generate raw payloads
        if args.module == "sqli":
            raw_payloads = module.generate(
                db=args.db,
                injection_type=args.injection_type
            )
        else:
            raw_payloads = module.generate()

        # 3️ Process (encode, obfuscate, simulate defense)
        final_payloads = process_payloads(raw_payloads, args)

        # 4️ Export
        exporter = Exporter(output_format=args.format, filename=args.filename)
        exporter.export(final_payloads)

        # Optional runtime info
        print(Fore.MAGENTA + f"Module: {args.module} | Encoding: {args.encode} | Format: {args.format}")
        print(Fore.CYAN + "=" * 65)

    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
