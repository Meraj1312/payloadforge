import json
from typing import List, Dict


class Exporter:

    @staticmethod
    def to_terminal(data: List[Dict]) -> None:
        for item in data:
            print("=" * 50)
            print(f"Payload : {item['payload']}")
            print(f"Blocked : {item['blocked']}")
            print(f"Reason  : {item['reason']}")
        print("=" * 50)


    @staticmethod
    def to_json(data: List[Dict], filename: str = "output.json") -> None:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


    @staticmethod
    def to_txt(data: List[Dict], filename: str = "output.txt") -> None:
        with open(filename, "w") as f:
            for item in data:
                f.write(f"{item}\n")
