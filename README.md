*PayloadForge*

A modular, educational payload generation framework for modeling common web exploitation patterns and defensive detection logic.

 *Installation & Module Execution*

Clone the repository:

git clone https://github.com/Meraj1312/payloadforge.git
cd payloadforge

Important:
To run PayloadForge correctly and avoid Python import issues, you must run it as a module using -m:

python -m payloadforge.payloadforge -m <module> [options]

Example:

python -m payloadforge.payloadforge -m sqli -f json

This ensures Python treats the project as a package, resolving imports like payloadforge.core.exporter.

Requirements:

Python 3.x

No external dependencies

🚀 Overview

PayloadForge is a Python-based framework designed for educational and defensive security research.

It generates structured payload templates for common web vulnerabilities and simulates how defensive systems may classify or block them.

This project focuses on understanding:

Exploitation patterns (in a controlled way)

Signature-based detection

Input filtering logic

Defensive response modeling

⚠️ Important Notice

✅ Generates payload templates only

✅ Simulates defensive analysis

❌ Does NOT execute payloads

❌ Does NOT perform network scanning

❌ Does NOT attack live systems

This tool is strictly intended for:

Security learning

CTF environments

Defensive research

Controlled lab testing

 Supported Modules
Module	Description
sqli	SQL Injection payload templates
xss	Cross-Site Scripting payload templates
cmdi	Command Injection payload templates
 Encoding Support

Payloads can be encoded using:

Option	Description
none	No encoding (default)
url	URL encoding
base64	Base64 encoding
hex	Hex encoding
Example
python -m payloadforge.payloadforge -m xss -e base64
 Obfuscation Support

Currently supported obfuscation mode:

Option	Description
case	Randomized case variation
Example

Original:

UNION SELECT username FROM users

Obfuscated:

uNiOn SeLeCt username FrOm users

This demonstrates how simple transformations may impact signature-based detection.

 Defense Intelligence Output

Each generated payload may include simulated defensive analysis.

Example output:

[Defense Info]
{
  'blocked': True,
  'detected_patterns': ['union select'],
  'risk_level': 'high',
  'reason': 'Matched known dangerous signatures'
}

This provides insight into:

Pattern matching detection

Risk classification

Signature triggers

Why a payload would be blocked

The goal is to bridge offensive modeling with defensive understanding.

 Export Formats

PayloadForge supports multiple export formats:

Format	Description
terminal	Print to CLI
json	Export JSON file
txt	Export plain text
burp	Burp Suite compatible list
zap	OWASP ZAP compatible list
all	Export all formats
 Default Filename Behavior

If no custom filename is provided using --filename, PayloadForge automatically generates a unique filename using this pattern:

payloadforge_<YYYYMMDD>_<HHMMSS>_<format>
Example

Command:

python -m payloadforge.payloadforge -m sqli -f zap

Generated file:

payloadforge_20260220_022513_zap

Where:

YYYYMMDD → Date

HHMMSS → Time

format → Selected export format

This ensures:

✅ Unique filenames

✅ No accidental overwriting

✅ Organized export history

Custom Filename
python -m payloadforge.payloadforge -m sqli -f json --filename custom_output

Generates:

custom_output.json
 CLI Help

To view all available options:

python -m payloadforge.payloadforge -h

Available arguments:

-m, --module        Required. Select module: sqli, xss, cmdi
-e, --encode        Encoding mode: none, url, base64, hex
-o, --obfuscate     Obfuscation mode (currently supports: case)
-f, --format        Output format: terminal, json, txt, burp, zap, all
--filename          Custom export filename
-h, --help          Show help message
 Usage Examples
Generate SQLi payloads
python -m payloadforge.payloadforge -m sqli
Generate XSS payloads with encoding
python -m payloadforge.payloadforge -m xss -e url
Generate CMDi payloads with obfuscation
python -m payloadforge.payloadforge -m cmdi -o case
Export to JSON
python -m payloadforge.payloadforge -m sqli -f json
Export all formats
python -m payloadforge.payloadforge -m xss -f all
🏗 Project Structure
payloadforge/
│
├── payloadforge.py
├── core/
│   ├── exporter.py
│   ├── generic_obfuscation.py
│   └── security_controls.py
├── encoders/
│   └── encode.py
├── modules/
│   ├── sqli/
│   ├── xss/
│   └── cmdi/
└── README.md

The architecture is modular and easily extendable for:

Additional vulnerability modules

Advanced obfuscation strategies

More encoding techniques

Enhanced defensive modeling

 Ethical Usage

This project is intended strictly for:

Educational purposes

Authorized security testing

Defensive research

Controlled lab environments

Users are responsible for ensuring legal and ethical usage.
