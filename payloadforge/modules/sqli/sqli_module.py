# modules/sqli/sqli_module.py
from typing import List
from core.base import BaseModule
from .sqli_payloads import SQLI_PAYLOADS

class SQLIModule(BaseModule):
    name = "sqli"

    def __init__(self):
        self.default_dbs = ["mysql", "postgresql", "mssql"]

    def generate(self, db: str = "all", injection_type: str = "all", **kwargs) -> List[str]:
        """
        Return a flat list of payload strings.
        Parameters are accepted for CLI->framework wiring, but no encoding/obf/defense runs here.
        """
        dbs = self.default_dbs if db == "all" else [db]
        types_map = {
            "error": ["error"],
            "union": ["union"],
            "blind": ["blind_boolean", "blind_time"],
            "comment_bypass": ["comment_bypass"],
            "case_variation": ["case_variation"],
            "all": ["error", "union", "blind_boolean", "blind_time", "comment_bypass", "case_variation"]
        }
        types = types_map.get(injection_type, types_map["all"])

        payloads: List[str] = []
        for db_name in dbs:
            db_map = SQLI_PAYLOADS.get(db_name, {})
            for typ in types:
                items = db_map.get(typ, [])
                for p in items:
                    payloads.append(p)
        return payloads
