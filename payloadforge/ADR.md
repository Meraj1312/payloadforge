# Architecture Decision Record – PayloadForge

## ADR-001: Modular Vulnerability Design

### Decision
Each vulnerability type (SQLi, XSS, CMDI) is implemented as a separate module.

### Rationale
- Clear separation of concerns
- Easier maintenance
- Extensible architecture
- Allows future plugin-based design

### Consequences
New modules (e.g., SSTI, LFI) can be added without modifying core logic.

---

## ADR-002: Layered Processing Pipeline

### Decision
Payload processing follows a layered architecture:

1. Raw payload generation
2. Encoding layer
3. Obfuscation layer
4. Security simulation layer
5. Output formatting

### Rationale
- Mirrors real-world attack transformation stages
- Encourages mental modeling of payload evolution
- Improves testability

---

## ADR-003: No Active Exploitation

### Decision
PayloadForge does not send requests or execute attacks.

### Rationale
- Ethical alignment
- Academic safety
- Prevent misuse
- Defensive-focused learning

---

## ADR-004: Simulation-Based Security Controls

### Decision
Security controls are simulated using pattern detection logic.

### Rationale
- Demonstrates how WAFs and filters identify payload signatures
- Avoids real bypass automation
- Maintains educational focus

---

## ADR-005: CLI-Driven Interface

### Decision
The framework uses a CLI interface instead of GUI.

### Rationale
- Lightweight
- Professional tool style
- Easier integration into security workflows
- Matches common security tooling ecosystems

---

## Future Consideration

- Plugin-based module loader
- Chained encoding support
- YAML configuration support
