#!/usr/bin/env python3
"""
Simple SQL Injection Module for PayloadForge
"""

import json
from datetime import datetime
from .sqli_payloads import PayloadTemplates
from .sqli_obfuscation import SQLObfuscator
from .sqli_signatures import DatabaseSignatures


class SQLiModule:
    """Main SQL Injection Module with generate() method"""
    
    def __init__(self):
        self.name = "SQL Injection Module"
        self.templates = PayloadTemplates()
        self.obfuscator = SQLObfuscator()
        self.signatures = DatabaseSignatures()
    
    def generate(self, sqli_type="all", database="all", obfuscation=None, encode=None):
        """
        Generate SQL injection payload templates
        
        Args:
            sqli_type: error_based, union_based, blind_boolean, blind_time, all
            database: mysql, postgresql, mssql, oracle, all
            obfuscation: list of techniques ['case', 'space', 'comment']
            encode: url, base64, hex
        """
        # Get payloads
        if sqli_type == "all":
            payloads = self.templates.get_all()
        else:
            payloads = self.templates.get_by_type(sqli_type)
        
        # Filter by database
        if database != "all":
            payloads = [p for p in payloads if p.get("db_type") == database]
        
        # Apply obfuscation
        if obfuscation:
            for tech in obfuscation:
                for p in payloads:
                    if tech == "case":
                        p["obfuscated"] = self.obfuscator.case_obfuscation(p["payload"])
                    elif tech == "space":
                        p["obfuscated"] = self.obfuscator.space_obfuscation(p["payload"], p.get("db_type", "mysql"))
                    elif tech == "comment":
                        p["obfuscated"] = self.obfuscator.comment_obfuscation(p["payload"], p.get("db_type", "mysql"))
        
        # Apply encoding
        if encode:
            for p in payloads:
                if encode == "url":
                    from urllib.parse import quote
                    p["encoded"] = quote(p["payload"])
                elif encode == "base64":
                    import base64
                    p["encoded"] = base64.b64encode(p["payload"].encode()).decode()
                elif encode == "hex":
                    p["encoded"] = p["payload"].encode().hex()
        
        # Add signatures info
        for p in payloads:
            db = p.get("db_type", "generic")
            p["signatures"] = self.signatures.get_keywords(db)[:5]  # First 5 keywords
        
        # Build result
        return {
            "metadata": {
                "module": self.name,
                "type": sqli_type,
                "database": database,
                "generated": str(datetime.now()),
                "total": len(payloads)
            },
            "payloads": payloads
        }
    
    def to_json(self, catalog):
        """Convert to JSON"""
        return json.dumps(catalog, indent=2)
    
    def to_txt(self, catalog):
        """Convert to readable text"""
        lines = []
        lines.append("="*50)
        lines.append(f"SQL INJECTION PAYLOADS ({catalog['metadata']['type']})")
        lines.append("="*50)
        
        for i, p in enumerate(catalog['payloads'], 1):
            lines.append(f"\n{i}. {p['type']} - {p['db_type']}")
            lines.append(f"   Payload: {p['payload']}")
            if 'obfuscated' in p:
                lines.append(f"   Obfuscated: {p['obfuscated']}")
            if 'encoded' in p:
                lines.append(f"   Encoded: {p['encoded']}")
            lines.append(f"   Desc: {p['description']}")
        
        return "\n".join(lines)
