"""
PayloadForge - Educational Payload Generation Framework
Main Controller
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

#Banner
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from pyfiglet import Figlet
from colorama import init, Fore

init(autoreset=True)
console = Console()


def show_banner():
    f = Figlet(font="slant")  # Try: doom, big, cyberlarge
    banner = f.renderText("PayloadForge")

    console.print(f"[bold magenta]{banner}[/bold magenta]")
    console.print(
        Panel.fit(
            "[bold cyan]Educational Payload Generation Framework[/bold cyan]\n"
            "[dim]Author: Meraj | Offensive Security Lab[/dim]",
            border_style="bright_magenta",
        )
    )



def get_module(module_name: str):
    module_map = {
        "sqli": SQLIModule,
        "xss": XSSModule,
        "cmdi": CMDIModule,
    }

    if module_name not in module_map:
        raise ValueError(f"Unsupported module: {module_name}")

    return module_map[module_name]()


def process_payloads(payloads: list[dict], args) -> list[dict]:
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
                "context": item.get("context"),
                "os": item.get("os"),
                "defense": defense_result,
            }
        )

    return processed


def main():
    show_banner()

    parser = argparse.ArgumentParser(
        description="PayloadForge - Educational Payload Generator",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # =========================
    # Core Arguments
    # =========================
    parser.add_argument(
        "--module",
        required=True,
        choices=["sqli", "xss", "cmdi"],
        help="Select attack module (sqli, xss, cmdi)"
    )

    parser.add_argument(
        "--encode",
        default="none",
        choices=["none", "url", "base64", "hex"],
        help="Encoding mode"
    )

    parser.add_argument(
    "--obfuscate",
    default=None,
    choices=["case", "whitespace", "tabs", "all"],
    help="Obfuscation mode (options: case, whitespace, tabs, all)"
)
    # =========================
    # SQLi Arguments
    # =========================
    parser.add_argument(
        "--database",
        default="all",
        choices=["all", "mysql", "postgresql", "mssql"],
        help="Target database (SQLi only)"
    )

    parser.add_argument(
        "--sqli-type",
        default="all",
        choices=["all", "error", "union", "blind", "comment_bypass", "case_variation"],
        help="SQL Injection type"
    )

    # =========================
    # XSS Arguments
    # =========================
    parser.add_argument(
        "--xss-type",
        default="all",
        choices=["all", "reflected", "stored", "dom"],
        help="XSS vulnerability type"
    )

    parser.add_argument(
        "--context",
        default="all",
        choices=["all", "html", "attribute", "javascript"],
        help="XSS injection context"
    )

    # =========================
    # Export Arguments (آخر حاجتين)
    # =========================
    parser.add_argument(
        "--format",
        default="terminal",
        choices=["terminal", "json", "txt", "burp", "zap", "all"],
        help="Export format"
    )

    parser.add_argument(
        "--filename",
        default=None,
        help="Custom export filename (without extension)"
    )

    args = parser.parse_args()

    try:
        module = get_module(args.module)

        # Generate payloads depending on the module
        if args.module == "sqli":
            raw_payloads = module.generate(
                db=args.database,
                injection_type=args.sqli_type,
            )
        elif args.module == "xss":
            raw_payloads = module.generate(
                payload_type=args.xss_type,
                context=args.context,
            )
        else:  # CMDi
            raw_payloads = module.generate()

        final_payloads = process_payloads(raw_payloads, args)

        exporter = Exporter(
            output_format=args.format,
            filename=args.filename,
        )
        exporter.export(final_payloads)

        print(Fore.MAGENTA + f"Module: {args.module} | Encoding: {args.encode} | Format: {args.format}")
        print(Fore.CYAN + "=" * 65)

    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
