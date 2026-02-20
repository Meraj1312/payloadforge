# PayloadForge

## 1️⃣ Project Overview

PayloadForge is a modular, educational payload generation framework designed to demonstrate common web exploitation patterns and their corresponding defensive considerations.

This project is built strictly for **educational and defensive learning purposes**.

- Generates **payload templates only**
- Does **not execute** payloads
- Does **not automate attacks**
- Does **not interact with live systems**
- Does **not perform network or database operations**

The goal is to understand how vulnerabilities work and how they should be mitigated — not to exploit real systems.

---

## 2️⃣ Features

- Cross-Site Scripting (XSS) payload templates  
- SQL Injection (SQLi) payload templates  
- Command Injection (CMDi) payload templates  
- Encoding support (URL, Base64, Hex)  
- JSON and TXT export functionality  
- Modular architecture for clean extension  

---

## 3️⃣ Installation

```bash
git clone https://github.com/yourusername/payloadforge.git
cd payloadforge
No external dependencies are required beyond standard Python.
```
## 4️⃣ Usage Examples

```
python3 -m payloadforge.payloadforge -m sqli

python3 -m payloadforge.payloadforge -m xss -e url

python3 -m payloadforge.payloadforge -m cmdi -o case

python3 -m payloadforge.payloadforge -m sqli -f json --filename payloads

```
Supported Flags
`--module` → Select vulnerability module (xss, sqli, cmdi)

`--db` → Select database type (for SQLi module)

`--encode` → Apply encoding to generated payloads

`--output` → Choose export format (json or txt)

## 5️⃣ Project Structure
```
payloadforge/
│
├── payloadforge.py
│
├── core/
│   ├── base.py
│   ├── registry.py
│   └── exporter.py
│
├── modules/
│   ├── xss/
│   │   ├── payloads.py
│   │   ├── contexts.py
│   │   └── notes.py
│   │
│   ├── sqli/
│   │   ├── payloads.py
│   │   ├── databases.py
│   │   └── notes.py
│   │
│   ├── cmdi/
│   │   ├── payloads.py
│   │   ├── platforms.py
│   │   └── notes.py
│
├── encoders/
│   ├── url.py
│   ├── base64.py
│   └── hex.py
│
├── data/
│   └── sample_exports/
│
├── docs/
│   ├── ETHICS.md
│   ├── DEFENSIVE_NOTES.md
│   └── REFERENCES.md
│
└── README.md
```
## 6️⃣ Ethical Notice
PayloadForge is developed strictly for educational and defensive research purposes.

No live exploitation capabilities

No automated attack functionality

No system interaction or execution

Templates only

Users are responsible for ensuring all usage complies with applicable laws and ethical standards.

## 7️⃣ Team & Responsibilities

- [Muhammad Meraj](#muhammad-meraj) – Project Coordination & Documentation
- [Haris Elahi](#haris-elahi) – CLI Integration & Encoders
- [Rana Ahmed](#rana-ahmed) – Core Architecture & Defensive Notes
- [Muhammad Saady](#muhammad-saady) – Export & Output System
- [Areez Ahmad](#areez-ahmad) – XSS Module Developer
- [Sondos Sayed](#sondos-sayed) – SQL Injection Module Developer
- [Ali Abbas](#ali-abbas) – Command Injection Module Developer

---

### Muhammad Meraj
**Role:** Project Coordination & Documentation  

Oversees overall project structure and ensures consistency across modules.  
Responsible for writing `README.md`, `ETHICS.md`, and `REFERENCES.md`.  
Reviews module integration, maintains architectural consistency, and ensures the project aligns with ethical and educational objectives.

---

### Haris Elahi
**Role:** CLI Integration Engineer & Encoder Developer  

Implements `payloadforge.py` and handles CLI argument parsing (`--module`, `--encode`, `--db`, `--output`).  
Connects registry, modules, encoders, and exporter.  
Develops encoding modules in `encoders/` (`url.py`, `base64.py`, `hex.py`) and ensures full system integration.

---

### Rana Ahmed
**Role:** Core Architecture Engineer & Defensive Documentation  

Designs modular architecture in `core/base.py` and `core/registry.py`.  
Implements the `BaseModule` structure and module registration logic.  
Authors `DEFENSIVE_NOTES.md`, documenting prevention and mitigation strategies for demonstrated vulnerabilities.

---

### Muhammad Saady
**Role:** Export & Output Engineer  

Develops `core/exporter.py` to handle JSON and TXT export logic.  
Formats CLI output professionally and prepares structured sample exports in `data/sample_exports/`.

---

### Areez Ahmad
**Role:** XSS Module Developer  

Develops the XSS module in `modules/xss/`.  
Creates payload templates for Reflected, Stored, and DOM-based XSS.  
Implements context awareness (HTML, Attribute, JavaScript contexts) and adds defensive notes and bypass explanations.

---

### Sondos Sayed
**Role:** SQL Injection Module Developer  

Develops the SQL Injection module in `modules/sqli/`.  
Creates structured templates for Error-based, Union-based, and Blind SQLi (descriptive only).  
Implements database selection logic (MySQL, PostgreSQL, MSSQL) and adds defensive documentation.

---

### Ali Abbas
**Role:** Command Injection Module Developer  

Develops the Command Injection module in `modules/cmdi/`.  
Implements Linux and Windows command template patterns, separator examples, and conceptual filter bypass explanations.  
Adds defensive notes without enabling real command execution.

