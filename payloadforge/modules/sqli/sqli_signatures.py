# modules/sqli/sqli_signatures.py

# SQLi-specific patterns and short explanations.
SQLI_SIGNATURES = {
    "UNION SELECT": "Classic UNION-based SQL injection pattern.",
    "SLEEP": "Time-based SQLi attempt (MySQL).",
    "BENCHMARK": "Time-based SQLi attempt (MySQL).",
    "WAITFOR": "Time-based SQLi attempt (MSSQL).",
    "EXTRACTVALUE": "Error-based SQLi using XML function.",
    "UPDATEXML": "Error-based SQLi using XML function.",
    "CONVERT": "Potential error-based SQLi pattern.",
    "' OR '": "Boolean-based SQL injection pattern.",
    "1=1": "Tautology used in authentication bypass."
}

SQLI_FILTER_NOTES = {
    "addslashes()": "Adds backslashes before quotes.",
    "mysqli_real_escape_string()": "Escapes special characters.",
    "parameterized query": "Prevents injection completely.",
    "magic_quotes_gpc": "Deprecated but adds slashes."
}

SQLI_VALIDATOR_BEHAVIOR = {
    "integer validation": "FAIL - contains non-numeric characters.",
    "email validation": "FAIL - not a valid email format.",
    "whitelist": "PASS only if value is in allowed list.",
    "length check": "PASS if within allowed length."
}

MODERN_DEFENSE_NOTE = (
    "Modern WAFs normalize input by decoding URL/Base64, "
    "removing comments, and lowercasing before signature matching."
)
