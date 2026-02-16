from sqli_payloads import SQLI_PAYLOADS
from sqli_defenses import SQLiDefenseAnalyzer
from sqli_encoder import SQLiEncoder
from sqli_obfuscator import SQLiObfuscator
from sqli_output import SQLiOutput

class SQLiGenerator:
    def __init__(self, db="all", injection_type="all", encode=None, obfuscate=False):
        self.db = db
        self.injection_type = injection_type
        self.encode = encode
        self.obfuscate = obfuscate

    def generate(self):
        """Generate list of payload dictionaries with defenses."""
        payloads = []
        # Determine which databases
        dbs = ["mysql", "postgresql", "mssql"] if self.db == "all" else [self.db]
        # Determine which types
        types_map = {
            "error": ["error"],
            "union": ["union"],
            "blind": ["blind_boolean", "blind_time"],
            "comment_bypass": ["comment_bypass"],
            "case_variation": ["case_variation"],
            "all": ["error", "union", "blind_boolean", "blind_time", "comment_bypass", "case_variation"]
        }
        types = types_map.get(self.injection_type, ["error", "union", "blind_boolean", "blind_time", "comment_bypass", "case_variation"])
        pid = 1
        for db in dbs:
            for typ in types:
                # Get payload list for this db and typ
                pay_list = SQLI_PAYLOADS.get(db, {}).get(typ, [])
                for pay in pay_list:
                    # Get defense info
                    waf_resp = SQLiDefenseAnalyzer.get_waf_response(pay, db)
                    filter_resp = SQLiDefenseAnalyzer.get_filter_response(pay, db)
                    val_resp = SQLiDefenseAnalyzer.get_validator_response(pay, db)
                    why = SQLiDefenseAnalyzer.why_blocked(pay, db)
                    modern = SQLiDefenseAnalyzer.modern_defense_evasion(pay, db)
                    
                    payload_item = {
                        "id": pid,
                        "payload": pay,
                        "database": db,
                        "type": typ,
                        "defense": {
                            "waf": str(waf_resp),
                            "filter": str(filter_resp),
                            "validator": str(val_resp),
                            "why": why,
                            "modern": modern
                        }
                    }
                    payloads.append(payload_item)
                    pid += 1

        # Apply encoding if requested
        if self.encode and self.encode != "none":
            payloads = SQLiEncoder.encode_all(payloads, self.encode)

        # Apply obfuscation if requested
        if self.obfuscate:
            payloads = SQLiObfuscator.obfuscate_all(payloads)

        return payloads

    def output(self, format, filename=None):
        """Generate and output in specified format."""
        payloads = self.generate()
        out = SQLiOutput(payloads)
        if format == "terminal":
            out.to_terminal()
        elif format == "json":
            out.to_json(filename)
        elif format == "txt":
            out.to_txt(filename)
        elif format == "burp":
            out.to_burp(filename)
        elif format == "zap":
            out.to_zap(filename)
        elif format == "all":
            out.to_terminal()
            out.to_json(filename)
            out.to_txt(filename)
            out.to_burp(filename)
            out.to_zap(filename)