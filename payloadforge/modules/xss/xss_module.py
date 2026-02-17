#!/usr/bin/env python3
"""
XSS Module - Main module file
Educational Purpose Only - For Authorized Testing & Learning
"""

import json
import argparse
from typing import Dict, List, Any, Optional
from enum import Enum

from ...base_module import BaseModule
from .xss_payloads import XSSPayloads
from .xss_obfuscation import XSSObfuscation
from .xss_signatures import XSSSignatures

class ContextType(Enum):
    """XSS context types for payload generation"""
    HTML = "html"
    ATTRIBUTE = "attribute"
    JAVASCRIPT = "javascript"

class XSSModule(BaseModule):
    """
    Cross-Site Scripting Payload Generation Module
    Inherits from BaseModule
    """
    
    def __init__(self):
        super().__init__(
            name="XSS Payload Generator",
            description="Generates educational Cross-Site Scripting payload templates"
        )
        self.module_type = "xss"
        self.payloads = XSSPayloads()
        self.obfuscation = XSSObfuscation()
        self.signatures = XSSSignatures()
    
    def generate(self, **kwargs) -> Dict[str, Any]:
        """
        Main generate method - REQUIRED by BaseModule
        
        Args:
            context: html/attribute/javascript (from --context flag)
            payload_type: reflected/stored/dom/all (from --type flag)
            obfuscate: comment/whitespace/case (from --obfuscate flag)
            
        Returns:
            Dictionary with generated payloads
        """
        # Get parameters
        context = kwargs.get('context', 'html')
        payload_type = kwargs.get('payload_type', 'all')
        obfuscate = kwargs.get('obfuscate', None)
        
        # Convert string context to Enum
        context_enum = self._get_context_enum(context)
        
        # Generate catalog
        catalog = self.generate_payload_catalog(
            module_type=payload_type if payload_type != "all" else "all",
            context=context_enum
        )
        
        # Apply obfuscation if requested
        if obfuscate:
            for payload in catalog["payloads"]:
                obfuscated = self.obfuscation.obfuscate(
                    payload["payload"], 
                    obfuscate,
                    context
                )
                payload["obfuscated_version"] = {
                    "original": payload["payload"],
                    "obfuscated": obfuscated,
                    "technique": obfuscate,
                    "description": f"Bypass using {obfuscate.replace('_', ' ')}"
                }
        
        # Add defensive notes from signatures
        catalog["defensive_notes"] = self.signatures.get_defensive_notes(context)
        catalog["bypass_techniques"] = self.signatures.get_bypass_techniques()
        
        return catalog
    
    def _get_context_enum(self, context_str: str) -> ContextType:
        """Convert string context to ContextType Enum"""
        context_map = {
            "html": ContextType.HTML,
            "attribute": ContextType.ATTRIBUTE,
            "javascript": ContextType.JAVASCRIPT
        }
        return context_map.get(context_str, ContextType.HTML)
    
    def generate_payload_catalog(self, module_type: str = "all", context: ContextType = None) -> Dict:
        """Generate complete payload catalog with all variations"""
        catalog = {
            "metadata": self.get_metadata(),
            "payloads": []
        }
        
        contexts = [ContextType.HTML, ContextType.ATTRIBUTE, ContextType.JAVASCRIPT]
        
        # If specific context provided, use only that
        if context:
            contexts = [context]
        
        for ctx in contexts:
            if module_type == "all" or module_type == "reflected":
                for payload in self.payloads.get_reflected(ctx):
                    catalog["payloads"].append({
                        "type": "reflected",
                        "context": ctx.value,
                        **payload
                    })
            
            if module_type == "all" or module_type == "stored":
                for payload in self.payloads.get_stored(ctx):
                    catalog["payloads"].append({
                        "type": "stored",
                        "context": ctx.value,
                        **payload
                    })
            
            if module_type == "all" or module_type == "dom":
                for payload in self.payloads.get_dom_based(ctx):
                    catalog["payloads"].append({
                        "type": "dom",
                        "context": ctx.value,
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
        output.append(f"XSS EDUCATIONAL PAYLOAD CATALOG")
        output.append("=" * 60)
        output.append(f"Purpose: Educational - Payload Templates for Learning")
        output.append(f"Ethical Use Only: True")
        output.append("=" * 60 + "\n")
        
        for payload in catalog["payloads"]:
            output.append(f"[{payload['type'].upper()}] Context: {payload['context']}")
            output.append(f"Payload: {payload['payload']}")
            output.append(f"Description: {payload['description']}")
            output.append(f"Bypass Techniques: {', '.join(payload.get('bypass_techniques', []))}")
            
            if 'storage_medium' in payload:
                output.append(f"Storage Medium: {', '.join(payload['storage_medium'])}")
                output.append(f"Trigger: {payload['trigger_condition']}")
            
            if 'source' in payload:
                output.append(f"DOM Source: {payload['source']}")
                output.append(f"DOM Sink: {payload['sink']}")
            
            if 'obfuscated_version' in payload:
                output.append(f"Obfuscated: {payload['obfuscated_version']['obfuscated']}")
                output.append(f"Technique: {payload['obfuscated_version']['technique']}")
            
            output.append("-" * 40)
        
        return "\n".join(output)
    
    def get_metadata(self) -> Dict[str, Any]:
        """Return module metadata"""
        base_metadata = super().get_metadata()
        base_metadata.update({
            "tool": "XSS Educational Generator",
            "purpose": "Educational - Payload Templates for Learning",
            "ethical_use_only": True,
            "reference": "PortSwigger XSS Cheat Sheet",
            "supported_contexts": ["html", "attribute", "javascript"],
            "supported_types": ["reflected", "stored", "dom"],
            "obfuscation_options": ["comment", "whitespace", "case"]
        })
        return base_metadata


# CLI interface
def main():
    """CLI interface for XSS Payload Generator"""
    parser = argparse.ArgumentParser(
        description="XSS Educational Payload Generator",
        epilog="For authorized testing and educational purposes only"
    )
    
    parser.add_argument("--module", choices=["xss"], default="xss",
                       help="Module to use (xss only for this version)")
    parser.add_argument("--type", choices=["reflected", "stored", "dom", "all"],
                       default="all", help="Type of XSS payloads")
    parser.add_argument("--context", choices=["html", "attribute", "javascript"],
                       default="html", help="Context for payload generation")
    parser.add_argument("--obfuscate", choices=["comment", "whitespace", "case"],
                       help="Apply obfuscation technique")
    parser.add_argument("--output", choices=["json", "txt"], default="json",
                       help="Output format")
    parser.add_argument("--export", type=str, help="Export to file")
    
    args = parser.parse_args()
    
    # Initialize module
    module = XSSModule()
    
    # Generate catalog
    catalog = module.generate(
        context=args.context,
        payload_type=args.type,
        obfuscate=args.obfuscate
    )
    
    # Output results
    output_data = module.export_payloads(catalog, args.output)
    
    if args.export:
        with open(args.export, 'w') as f:
            f.write(output_data)
        print(f"[+] Payload catalog exported to {args.export}")
    else:
        print(output_data)

if __name__ == "__main__":
    main()
