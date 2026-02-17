#!/usr/bin/env python3
"""
XSS Signatures - Keywords and patterns dictionary
Contains all XSS-related signatures, contexts, and defensive notes
ITSOLERA Internship Task - Educational Purpose Only
"""

from typing import Dict, List, Any

class XSSSignatures:
    """Repository of XSS keywords, contexts, and defensive information"""
    
    # Context definitions
    CONTEXTS = {
        "html": {
            "name": "HTML Context",
            "description": "Payload injected directly into HTML",
            "delimiters": ["<", ">"],
            "dangerous_tags": ["script", "img", "svg", "body", "iframe", "object", "embed", "details"],
            "dangerous_attributes": ["onload", "onerror", "onmouseover", "onfocus", "onclick", "ontoggle"]
        },
        "attribute": {
            "name": "Attribute Context",
            "description": "Payload injected into HTML attribute values",
            "delimiters": ["\"", "'", "=", "`"],
            "dangerous_prefixes": ["javascript:", "data:", "vbscript:"],
            "dangerous_events": ["onmouseover", "onclick", "onfocus", "onblur", "onload", "onerror", "onchange"]
        },
        "javascript": {
            "name": "JavaScript Context",
            "description": "Payload injected into JavaScript code",
            "delimiters": ["'", '"', '`', ';', '/', '\\'],
            "dangerous_functions": ["eval", "setTimeout", "setInterval", "Function", "execScript", "alert"],
            "dangerous_properties": ["innerHTML", "outerHTML", "document.write", "location", "cookie"]
        }
    }
    
    # Payload type definitions
    PAYLOAD_TYPES = {
        "reflected": {
            "name": "Reflected XSS",
            "description": "Payload comes from current HTTP request",
            "characteristics": ["non-persistent", "immediate", "request-based", "single-use"]
        },
        "stored": {
            "name": "Stored XSS",
            "description": "Payload stored on target server",
            "characteristics": ["persistent", "database-backed", "affects multiple users", "high-impact"]
        },
        "dom": {
            "name": "DOM-based XSS",
            "description": "Payload executed via DOM manipulation",
            "characteristics": ["client-side", "source-sink", "no server interaction", "harder to detect"]
        }
    }
    
    # Event handlers dictionary
    EVENT_HANDLERS = [
        "onload", "onerror", "onclick", "onmouseover", "onmouseout",
        "onfocus", "onblur", "onsubmit", "onreset", "onchange",
        "onselect", "onkeydown", "onkeypress", "onkeyup", "ondblclick",
        "onunload", "onabort", "onresize", "onscroll", "oncontextmenu",
        "oninput", "oninvalid", "oncanplay", "onplaying", "onprogress",
        "ontoggle", "onvolumechange", "onwaiting"
    ]
    
    # HTML tags that can execute JavaScript
    DANGEROUS_TAGS = [
        "script", "img", "svg", "body", "iframe", "object", "embed",
        "video", "audio", "input", "button", "form", "details", "select",
        "textarea", "keygen", "marquee", "frameset", "frame", "style",
        "math", "noscript", "isindex"
    ]
    
    # JavaScript functions that can execute code
    DANGEROUS_FUNCTIONS = [
        "eval", "setTimeout", "setInterval", "Function", "execScript",
        "alert", "confirm", "prompt", "open", "fetch", "XMLHttpRequest",
        "atob", "btoa", "decodeURI", "encodeURI"
    ]
    
    # Common XSS sources for DOM-based
    DOM_SOURCES = [
        "document.URL", "document.documentURI", "document.baseURI",
        "location.href", "location.search", "location.hash", "location.pathname",
        "window.name", "document.referrer", "document.cookie", 
        "localStorage", "sessionStorage", "window.postMessage"
    ]
    
    # Common XSS sinks for DOM-based
    DOM_SINKS = [
        "innerHTML", "outerHTML", "document.write", "document.writeln",
        "eval", "setTimeout", "setInterval", "Function", "execScript",
        "location", "location.href", "location.replace", "location.assign",
        "open", "postMessage", "element.src", "element.href"
    ]
    
    def get_defensive_notes(self, context: str = None) -> Dict[str, Any]:
        """
        Get defensive notes for XSS prevention
        Used in final output to explain mitigations
        """
        
        notes = {
            "general_prevention": [
                "Use Content Security Policy (CSP) headers with strict directives",
                "Implement input validation and output encoding",
                "Use context-aware escaping based on where data is placed",
                "Apply principle of least privilege",
                "Use HTTPOnly and Secure flags for cookies",
                "Sanitize HTML with libraries like DOMPurify",
                "Regular security testing and code reviews"
            ],
            "waf_detection": [
                "Modern WAFs use context-aware parsing, not just regex",
                "Pattern matching on known attack signatures",
                "Behavioral analysis of request patterns",
                "Heuristic detection of obfuscation techniques",
                "Machine learning models for anomaly detection",
                "Rate limiting and request profiling"
            ],
            "why_wafs_block": [
                "Pattern matching on <script> tags and event handlers",
                "Detection of javascript: URIs and data URIs",
                "Analysis of attribute context for quote breaking",
                "Identification of eval(), setTimeout() usage",
                "Recognition of common obfuscation patterns"
            ]
        }
        
        if context:
            context_notes = {
                "html": [
                    "HTML encode all user input (convert < to &lt;, > to &gt;)",
                    "Use textContent instead of innerHTML",
                    "Avoid using dangerouslySetInnerHTML in React",
                    "Use template engines with auto-escaping",
                    "Validate and sanitize HTML tags"
                ],
                "attribute": [
                    "Quote all attribute values (single or double quotes)",
                    "Validate against allowed values where possible",
                    "Encode special characters: \", ', =, `",
                    "Avoid using javascript: URLs entirely",
                    "Use CSP to restrict script sources"
                ],
                "javascript": [
                    "Avoid eval(), setTimeout with strings, and similar functions",
                    "Use JSON.parse instead of eval for JSON",
                    "Encode data before inserting into JavaScript",
                    "Use Content Security Policy to restrict script sources",
                    "Validate and sanitize all JavaScript input"
                ]
            }
            notes["context_specific"] = context_notes.get(context, [])
        
        return notes
    
    def get_bypass_techniques(self) -> Dict[str, str]:
        """Get explanation of common bypass techniques"""
        return {
            "tag_switching": "Alternative tags when script is blocked (img, svg, body, iframe)",
            "event_handlers": "Different attack vectors bypass tag filters (onerror, onload, onmouseover)",
            "quote_breaking": "Breaking out of quoted attributes with extra quotes",
            "protocol_abuse": "Using javascript:, data:, vbscript: URIs",
            "string_breaking": "Breaking JavaScript string contexts with quotes and semicolons",
            "comment_insertion": "Regex patterns break with unexpected comments (<!-- -->, /* */)",
            "tag_closure": "Closing and reopening tags to escape context",
            "fragment_abuse": "Using URL fragments (#) for DOM XSS",
            "parameter_pollution": "HTTP parameter pollution to confuse parsers",
            "eval_abuse": "Abusing eval(), setTimeout, and Function constructor",
            "attribute_injection": "Injecting into HTML attributes that execute JavaScript",
            "exfiltration": "Stealing data using fetch, XMLHttpRequest, Image objects",
            "object_abuse": "Using JavaScript objects to execute code",
            "escape_sequences": "Using \\, \\x escape sequences",
            "string_manipulation": "String concatenation to avoid detection",
            "function_abuse": "Using Function constructor and other methods",
            "data_uri": "Using data URIs with encoded content",
            "svg_injection": "Using SVG tags and attributes for XSS",
            "iframe_abuse": "Using iframes for JavaScript execution",
            "storage_abuse": "Accessing localStorage and sessionStorage"
        }
    
    def get_context_signatures(self, context: str) -> Dict[str, List[str]]:
        """Get signatures specific to a context"""
        return self.CONTEXTS.get(context, {})
    
    def get_all_signatures(self) -> Dict[str, Any]:
        """Get all signatures as a complete dictionary"""
        return {
            "contexts": self.CONTEXTS,
            "payload_types": self.PAYLOAD_TYPES,
            "event_handlers": self.EVENT_HANDLERS,
            "dangerous_tags": self.DANGEROUS_TAGS,
            "dangerous_functions": self.DANGEROUS_FUNCTIONS,
            "dom_sources": self.DOM_SOURCES,
            "dom_sinks": self.DOM_SINKS
        }
