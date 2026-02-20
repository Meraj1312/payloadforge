<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/10372204-f5ac-44f5-86f3-86eba417eeb7" />


# PayloadForge

A modular, educational payload generation framework for modeling common web exploitation patterns and defensive detection logic.

## Installation and Module Execution

Clone the repository:

```bash
git clone https://github.com/Meraj1312/payloadforge.git
cd payloadforge
```

**Important:**
To run PayloadForge correctly and avoid Python import issues, run it as a module using `-m`:

```bash
python -m payloadforge.payloadforge -m <module> [options]
```

**Example:**

```bash
python -m payloadforge.payloadforge -m sqli -f json
```

## Requirements

*   Python 3.x
*   No external dependencies

## Overview

PayloadForge is a Python-based framework for educational and defensive security research. It generates structured payload templates for common web vulnerabilities and simulates how defensive systems may classify or block them.



### Important Notice

*   Generates payload templates only
*   Simulates defensive analysis
*   Does NOT execute payloads
*   Does NOT perform network scanning
*   Does NOT attack live systems

### Intended For

*   Security learning
*   CTF environments
*   Defensive research
*   Controlled lab testing

## Supported Modules

| Module | Description                   |
|--------|-------------------------------|
| `sqli`   | SQL Injection payload templates |
| `xss`    | Cross-Site Scripting payload templates |
| `cmdi`   | Command Injection payload templates |

## Encoding Support

Payloads can be encoded using:

| Option   | Description       |
|----------|-------------------|
| `none`     | No encoding (default) |
| `url`      | URL encoding      |
| `base64`   | Base64 encoding   |
| `hex`      | Hex encoding      |

**Example:**

```bash
python -m payloadforge.payloadforge -m xss -e base64
```

## Obfuscation Support

Currently supported obfuscation modes:

| Option     | Description                       |
|------------|-----------------------------------|
| `case`       | Randomized case variation         |
| `whitespace` | Replace single spaces with multiple |
| `tabs`       | Replace spaces with tabs          |
| `all`        | Apply all obfuscation techniques  |

**Example:**

Original:

```
UNION SELECT username FROM users
```

Obfuscated:

```
uNiOn SeLeCt username FrOm users
```

This shows how simple transformations can impact signature-based detection.

## Defense Intelligence Output

Each generated payload may include simulated defensive analysis.

**Example:**

```json
[
  {
    "blocked": true,
    "detected_patterns": [
      "union select"
    ],
    "risk_level": "high",
    "reason": "Matched known dangerous signatures"
  }
]
```

### Provides Insight Into

*   Pattern matching detection
*   Risk classification
*   Signature triggers
*   Why a payload would be blocked

## Export Formats

PayloadForge supports multiple export formats:

| Format     | Description               |
|------------|---------------------------|
| `terminal` | Print to CLI              |
| `json`     | Export JSON file          |
| `txt`      | Export plain text         |
| `burp`     | Burp Suite compatible list |
| `zap`      | OWASP ZAP compatible list |
| `all`      | Export all formats        |

### Default Filename Behavior

If no custom filename is provided using `--filename`, PayloadForge generates a unique filename using this format:

`payloadforge_<YYYYMMDD>_<HHMMSS>_<format>`

**Example:**

```bash
python -m payloadforge.payloadforge -m sqli -f zap
```

Generated file:

`payloadforge_20260220_022513_zap`

Where:

*   `YYYYMMDD` → Date
*   `HHMMSS` → Time
*   `format` → Selected export format

### Custom Filename

```bash
python -m payloadforge.payloadforge -m sqli -f json --filename custom_output
```

Generates:

`custom_output.json`

## CLI Help

To view all available options:

```bash
python -m payloadforge.payloadforge -h
```

### Available Arguments

| Flag          | Description                                    |
|---------------|------------------------------------------------|
| `-m`, `--module`    | Required. Select module: `sqli`, `xss`, `cmdi` |
| `-e`, `--encode`    | Encoding mode: `none`, `url`, `base64`, `hex` |
| `-o`, `--obfuscate` | Obfuscation mode (currently supports: `case`)  |
| `-f`, `--format`    | Output format: `terminal`, `json`, `txt`, `burp`, `zap`, `all` |
| `--filename`  | Custom export filename                         |
| `-h`, `--help`      | Show help message                              |

## Usage Examples

*   Generate SQLi payloads:

    ```bash
    python -m payloadforge.payloadforge -m sqli
    ```

*   Generate XSS payloads with encoding:

    ```bash
    python -m payloadforge.payloadforge -m xss -e url
    ```

*   Generate CMDi payloads with obfuscation:

    ```bash
    python -m payloadforge.payloadforge -m cmdi -o case
    ```

*   Export to JSON:

    ```bash
    python -m payloadforge.payloadforge -m sqli -f json
    ```

*   Export all formats:

    ```bash
    python -m payloadforge.payloadforge -m xss -f all
    ```

## Project Structure

```
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
```

## Ethical Usage

This project is intended strictly for:

*   Educational purposes
*   Authorized security testing
*   Defensive research
*   Controlled lab environments

Users are responsible for ensuring legal and ethical usage.
