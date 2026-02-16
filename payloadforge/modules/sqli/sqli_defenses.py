# sqli_defenses.py

class SQLiDefenseAnalyzer:
    @staticmethod
    def get_waf_response(payload: str, db_type: str) -> dict:
        """Simulate WAF responses based on payload patterns."""
        responses = {}
        # Common WAFs
        wafs = ["Cloudflare", "AWS WAF", "ModSecurity", "F5", "Imperva"]
        
        # Detection logic (simplified)
        if "UNION SELECT" in payload.upper():
            for waf in wafs:
                responses[waf] = "BLOCK - UNION SELECT pattern detected"
        elif "SLEEP" in payload.upper() or "BENCHMARK" in payload.upper() or "WAITFOR" in payload.upper():
            for waf in wafs:
                responses[waf] = "BLOCK - Time-based SQLi detected"
        elif "extractvalue" in payload or "updatexml" in payload or "CONVERT" in payload:
            for waf in wafs:
                responses[waf] = "BLOCK - Error-based SQLi signature"
        elif "' OR '" in payload or "1=1" in payload:
            for waf in wafs:
                responses[waf] = "BLOCK - Boolean-based SQLi"
        else:
            # Some may allow
            for waf in wafs:
                responses[waf] = "ALLOW (no signature)"
        
        return responses

    @staticmethod
    def get_filter_response(payload: str, db_type: str) -> dict:
        """Simulate application-level filters."""
        filters = {
            "addslashes()": "Adds backslashes before quotes",
            "mysqli_real_escape_string()": "Escapes special characters",
            "parameterized query": "PREVENTS injection completely",
            "magic_quotes_gpc": "Deprecated but adds slashes"
        }
        # Add specific notes based on payload
        if "'" in payload:
            filters["Note"] = "Single quote detected; escaping may fail if not used properly."
        return filters

    @staticmethod
    def get_validator_response(payload: str, db_type: str) -> dict:
        """Simulate input validation."""
        validators = {
            "integer validation": "FAIL - contains non-numeric characters",
            "email validation": "FAIL - not an email",
            "whitelist": "PASS if value in allowed list",
            "length check": "PASS if within limits"
        }
        return validators

    @staticmethod
    def why_blocked(payload: str, db_type: str) -> str:
        """Explain why a WAF would block this payload."""
        if "UNION SELECT" in payload.upper():
            return "UNION SELECT is a classic SQL injection pattern that WAFs look for."
        if "SLEEP" in payload.upper() or "BENCHMARK" in payload.upper() or "WAITFOR" in payload.upper():
            return "Time-based payloads are flagged due to potential database performance impact."
        if "extractvalue" in payload or "updatexml" in payload:
            return "Error-based functions like extractvalue are heavily monitored."
        return "May be blocked by heuristic analysis if anomalous."

    @staticmethod
    def modern_defense_evasion(payload: str, db_type: str) -> str:
        """Explain how modern defenses detect evasion."""
        return "Modern WAFs decode URL/Base64, remove comments, and normalize case before matching signatures."
