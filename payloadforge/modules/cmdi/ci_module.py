#!/usr/bin/env python3
"""
Command Injection Module - Main CLI Interface
Educational payload generation framework for authorized security testing

Author: Security Research Team
Purpose: Educational demonstration of command injection patterns
License: Educational use only - Authorized testing environments only

ETHICAL DISCLAIMER:
This tool is developed strictly for educational, defensive, and authorized 
penetration testing environments. Any misuse outside legal authorization is 
strictly prohibited and may be illegal.

Aligned with:
- OWASP Code of Ethics
- Responsible disclosure principles
- Authorized penetration testing standards
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# Import our modules
from ci_payloads import (
    get_payloads, get_separators, get_context_payloads,
    list_all_categories, EDUCATIONAL_NOTES
)
from ci_obfuscation import CommandObfuscator, get_preset, OBFUSCATION_PRESETS
from ci_advanced_obfuscation import AdvancedObfuscator, ADVANCED_PRESETS
from ci_signatures import (
    analyze_payload, explain_detection, get_defense_recommendation,
    MODERN_DEFENSES, DEFENSE_SUMMARY
)

# Version info
VERSION = "1.0.0"
AUTHOR = "Security Research Team"

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    """Display tool banner with disclaimer"""
    banner = f"""
{Colors.CYAN}{'=' * 70}
{Colors.BOLD}COMMAND INJECTION PAYLOAD GENERATION FRAMEWORK{Colors.ENDC}
{Colors.CYAN}{'=' * 70}{Colors.ENDC}
Version: {VERSION}
Author: {AUTHOR}
Purpose: Educational Security Research

{Colors.YELLOW}⚠️  ETHICAL USE ONLY - AUTHORIZED TESTING ENVIRONMENTS ⚠️{Colors.ENDC}

This tool generates payload templates for:
• Security training and education
• Authorized penetration testing
• Defensive research and analysis
• CTF challenges and labs

{Colors.RED}UNAUTHORIZED USE IS PROHIBITED AND MAY BE ILLEGAL{Colors.ENDC}
{Colors.CYAN}{'=' * 70}{Colors.ENDC}
"""
    print(banner)

def print_disclaimer():
    """Print ethical disclaimer"""
    disclaimer = f"""
{Colors.YELLOW}{'=' * 70}
DISCLAIMER & TERMS OF USE
{'=' * 70}{Colors.ENDC}

By using this tool, you acknowledge and agree that:

1. This tool is for EDUCATIONAL and AUTHORIZED TESTING only
2. You have explicit permission to test target systems
3. Unauthorized access to systems is illegal
4. The authors assume NO LIABILITY for misuse
5. You will comply with all applicable laws and regulations

Aligned with:
• OWASP Ethical Testing Guidelines
• Responsible Disclosure Standards
• Legal penetration testing practices

{Colors.GREEN}[✓] I understand and accept these terms{Colors.ENDC}
{Colors.YELLOW}{'=' * 70}{Colors.ENDC}
"""
    print(disclaimer)

def format_payload_output(payload_info, obfuscated=None, analysis=None, explain=False):
    """
    Format payload for CLI output with all details
    
    Args:
        payload_info (dict): Base payload information
        obfuscated (dict): Obfuscation results (optional)
        analysis (dict): Defense analysis (optional)
        explain (bool): Include detailed explanations
    
    Returns:
        str: Formatted output
    """
    output = []
    
    # Header
    output.append(f"\n{Colors.CYAN}{'━' * 70}{Colors.ENDC}")
    output.append(f"{Colors.BOLD}[TEMPLATE] Command Injection Payload{Colors.ENDC}")
    output.append(f"{Colors.CYAN}{'━' * 70}{Colors.ENDC}")
    
    # Basic info
    output.append(f"\n{Colors.BOLD}Payload ID:{Colors.ENDC} {payload_info.get('id', 'N/A')}")
    output.append(f"{Colors.BOLD}Base Payload:{Colors.ENDC} {payload_info['payload']}")
    output.append(f"{Colors.BOLD}Description:{Colors.ENDC} {payload_info.get('description', 'N/A')}")
    output.append(f"{Colors.BOLD}Context:{Colors.ENDC} {payload_info.get('context', 'N/A')}")
    output.append(f"{Colors.BOLD}Risk Level:{Colors.ENDC} {Colors.RED}{payload_info.get('risk', 'N/A').upper()}{Colors.ENDC}")
    
    # Obfuscation info
    if obfuscated:
        output.append(f"\n{Colors.BOLD}[OBFUSCATION APPLIED]{Colors.ENDC}")
        if 'final_payload' in obfuscated:
            output.append(f"{Colors.GREEN}Obfuscated:{Colors.ENDC} {obfuscated['final_payload']}")
        elif 'obfuscated' in obfuscated:
            output.append(f"{Colors.GREEN}Obfuscated:{Colors.ENDC} {obfuscated['obfuscated']}")
        elif 'encoded' in obfuscated:
            output.append(f"{Colors.GREEN}Encoded:{Colors.ENDC} {obfuscated['encoded']}")
        
        output.append(f"{Colors.BOLD}Technique:{Colors.ENDC} {obfuscated.get('technique', 'N/A')}")
        output.append(f"{Colors.BOLD}Bypass Reason:{Colors.ENDC} {obfuscated.get('bypass_reason', 'N/A')}")
        
        if 'transformation_steps' in obfuscated:
            output.append(f"\n{Colors.BOLD}Transformation Steps:{Colors.ENDC}")
            for step in obfuscated['transformation_steps']:
                if isinstance(step, dict):
                    output.append(f"  {step['step']}. {step['technique']}: {step['output']}")
                else:
                    output.append(f"  {step}")
    
    # Analysis info
    if analysis and explain:
        output.append(f"\n{Colors.BOLD}[DEFENSE ANALYSIS]{Colors.ENDC}")
        output.append(f"{Colors.BOLD}Risk Level:{Colors.ENDC} {Colors.RED}{analysis['risk_level'].upper()}{Colors.ENDC}")
        output.append(f"{Colors.BOLD}Detection Probability:{Colors.ENDC} {analysis['detection_probability']}")
        
        if analysis.get('dangerous_chars'):
            output.append(f"{Colors.YELLOW}Dangerous Chars:{Colors.ENDC} {', '.join(analysis['dangerous_chars'])}")
        
        if analysis.get('bypass_techniques'):
            output.append(f"{Colors.GREEN}Bypass Techniques:{Colors.ENDC} {', '.join(analysis['bypass_techniques'])}")
        
        if analysis.get('detected_patterns'):
            output.append(f"\n{Colors.BOLD}Detection Patterns Matched:{Colors.ENDC}")
            for pattern in analysis['detected_patterns']:
                output.append(f"  • {pattern['pattern']}: {pattern['description']} [{pattern['effectiveness']}]")
    
    # Example usage
    if 'example_vulnerable' in payload_info:
        output.append(f"\n{Colors.BOLD}Example Vulnerable Code:{Colors.ENDC}")
        output.append(f"  {payload_info['example_vulnerable']}")
    
    # Footer warning
    output.append(f"\n{Colors.YELLOW}[⚠️  WARNING] This is an educational template only!{Colors.ENDC}")
    output.append(f"{Colors.YELLOW}No execution capability - For authorized testing only{Colors.ENDC}")
    output.append(f"{Colors.CYAN}{'━' * 70}{Colors.ENDC}\n")
    
    return '\n'.join(output)

def generate_json_output(payloads_list, output_file=None):
    """
    Generate JSON format output
    
    Args:
        payloads_list (list): List of payload dictionaries
        output_file (str): Optional file path to save
    
    Returns:
        str: JSON formatted string
    """
    output_data = {
        'tool': 'Command Injection Module',
        'version': VERSION,
        'generated': datetime.now().isoformat(),
        'disclaimer': 'For authorized testing only',
        'payloads': payloads_list
    }
    
    json_str = json.dumps(output_data, indent=2)
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(json_str)
        print(f"{Colors.GREEN}[✓] JSON output saved to: {output_file}{Colors.ENDC}")
    
    return json_str

def generate_txt_catalog(payloads_list, output_file='payloads_catalog.txt'):
    """
    Generate text catalog of all payloads
    
    Args:
        payloads_list (list): List of payload dictionaries
        output_file (str): File path to save catalog
    """
    with open(output_file, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("COMMAND INJECTION PAYLOAD CATALOG\n")
        f.write("=" * 70 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Payloads: {len(payloads_list)}\n")
        f.write("=" * 70 + "\n\n")
        
        for i, payload in enumerate(payloads_list, 1):
            f.write(f"[{i}] {payload.get('id', 'N/A')}\n")
            f.write("-" * 70 + "\n")
            f.write(f"Payload: {payload['payload']}\n")
            f.write(f"Description: {payload.get('description', 'N/A')}\n")
            f.write(f"Context: {payload.get('context', 'N/A')}\n")
            f.write(f"Risk: {payload.get('risk', 'N/A')}\n")
            
            if 'obfuscated' in payload:
                f.write(f"Obfuscated: {payload['obfuscated']}\n")
            
            f.write("\n")
        
        f.write("=" * 70 + "\n")
        f.write("⚠️  FOR AUTHORIZED TESTING ONLY - EDUCATIONAL PURPOSES\n")
        f.write("=" * 70 + "\n")
    
    print(f"{Colors.GREEN}[✓] Text catalog saved to: {output_file}{Colors.ENDC}")

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description='Command Injection Payload Generation Framework (Educational)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate basic Linux payloads
  %(prog)s --os linux --category basic
  
  # Generate Windows payloads with URL encoding
  %(prog)s --os windows --category basic --encode url
  
  # Advanced brace expansion technique
  %(prog)s --os linux --advanced --technique brace
  
  # Generate all techniques with explanations
  %(prog)s --os linux --category filter_bypass --explain
  
  # Export to JSON for Burp Suite
  %(prog)s --os linux --category advanced --output json --file payloads.json
  
  # Show defense analysis
  %(prog)s --os linux --category basic --explain --defense

For more information, visit: https://owasp.org/www-project-web-security-testing-guide/
        """
    )
    
    # Basic options
    parser.add_argument('--os', choices=['linux', 'windows', 'both'], default='linux',
                       help='Target operating system')
    parser.add_argument('--category', choices=['basic', 'blind', 'advanced', 'filter_bypass', 'all'],
                       default='basic', help='Payload category')
    parser.add_argument('--context', choices=['parameter', 'filename', 'header', 'all'],
                       help='Injection context (optional)')
    
    # Obfuscation options
    parser.add_argument('--encode', choices=['url', 'url_double', 'base64', 'hex', 'unicode', 'none'],
                       help='Encoding technique')
    parser.add_argument('--obfuscate', choices=['quote', 'backslash', 'variable', 'ifs', 'wildcard', 
                       'case', 'brace', 'all'], help='Obfuscation method')
    parser.add_argument('--preset', choices=list(OBFUSCATION_PRESETS.keys()),
                       help='Use obfuscation preset')
    
    # Advanced options
    parser.add_argument('--advanced', action='store_true',
                       help='Enable advanced obfuscation techniques')
    parser.add_argument('--technique', choices=['brace', 'reverse', 'arithmetic', 'all'],
                       help='Advanced technique (requires --advanced)')
    parser.add_argument('--complexity', type=int, choices=[1, 2, 3, 4, 5],
                       default=1, help='Complexity level for advanced techniques')
    
    # Output options
    parser.add_argument('--output', choices=['cli', 'json', 'txt', 'all'], default='cli',
                       help='Output format')
    parser.add_argument('--file', help='Output file path (for json/txt)')
    parser.add_argument('--explain', action='store_true',
                       help='Show detailed explanations')
    parser.add_argument('--defense', action='store_true',
                       help='Show defense recommendations')
    
    # Utility options
    parser.add_argument('--list-categories', action='store_true',
                       help='List available categories')
    parser.add_argument('--list-techniques', action='store_true',
                       help='List available obfuscation techniques')
    parser.add_argument('--examples', action='store_true',
                       help='Show usage examples')
    parser.add_argument('--no-banner', action='store_true',
                       help='Suppress banner and disclaimer')
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    
    args = parser.parse_args()
    
    # Show banner unless suppressed
    if not args.no_banner:
        print_banner()
        print_disclaimer()
    
    # Handle utility options
    if args.list_categories:
        print(f"\n{Colors.BOLD}Available Categories:{Colors.ENDC}")
        print(f"\n{Colors.CYAN}Linux:{Colors.ENDC}")
        for cat in list_all_categories('linux'):
            print(f"  • {cat}")
        print(f"\n{Colors.CYAN}Windows:{Colors.ENDC}")
        for cat in list_all_categories('windows'):
            print(f"  • {cat}")
        return
    
    if args.list_techniques:
        print(f"\n{Colors.BOLD}Standard Obfuscation Techniques:{Colors.ENDC}")
        print("  • url - URL encoding")
        print("  • base64 - Base64 encoding")
        print("  • hex - Hexadecimal encoding")
        print("  • quote - Quote injection")
        print("  • backslash - Backslash escaping")
        print("  • variable - Variable expansion")
        print("  • ifs - IFS space bypass")
        print("  • wildcard - Wildcard obfuscation")
        print("  • case - Case variation (Windows)")
        
        print(f"\n{Colors.BOLD}Advanced Techniques:{Colors.ENDC}")
        print("  • brace - Brace expansion abuse")
        print("  • reverse - String reversal")
        print("  • arithmetic - Arithmetic expansion")
        
        print(f"\n{Colors.BOLD}Presets:{Colors.ENDC}")
        for preset, info in OBFUSCATION_PRESETS.items():
            print(f"  • {preset}: {info['description']} [{info['evasion_level']}]")
        return
    
    if args.examples:
        print(f"\n{Colors.BOLD}Usage Examples:{Colors.ENDC}\n")
        examples = [
            ("Basic payloads", "python ci_module.py --os linux --category basic"),
            ("URL encoded", "python ci_module.py --os windows --encode url"),
            ("Filter bypasses", "python ci_module.py --os linux --category filter_bypass"),
            ("Advanced brace", "python ci_module.py --os linux --advanced --technique brace"),
            ("With explanations", "python ci_module.py --os linux --category basic --explain"),
            ("JSON export", "python ci_module.py --os linux --output json --file payloads.json"),
            ("Text catalog", "python ci_module.py --os linux --category all --output txt"),
        ]
        for desc, cmd in examples:
            print(f"{Colors.CYAN}{desc}:{Colors.ENDC}")
            print(f"  {cmd}\n")
        return
    
    # Initialize obfuscators
    std_obfuscator = CommandObfuscator()
    adv_obfuscator = AdvancedObfuscator()
    
    # Get base payloads
    os_list = ['linux', 'windows'] if args.os == 'both' else [args.os]
    categories = list_all_categories(args.os) if args.category == 'all' else [args.category]
    
    all_payloads = []
    
    for os_type in os_list:
        for category in categories:
            if category in list_all_categories(os_type):
                payloads = get_payloads(os_type, category)
                
                for payload_info in payloads:
                    result = payload_info.copy()
                    result['os'] = os_type
                    result['category'] = category
                    
                    base_payload = payload_info['payload']
                    obfuscated_result = None
                    
                    # Apply standard obfuscation
                    if args.encode:
                        if args.encode == 'url':
                            obfuscated_result = std_obfuscator.url_encode(base_payload, double=False)
                        elif args.encode == 'url_double':
                            obfuscated_result = std_obfuscator.url_encode(base_payload, double=True)
                        elif args.encode == 'base64':
                            obfuscated_result = std_obfuscator.base64_encode(base_payload.strip('; '))
                        elif args.encode == 'hex':
                            obfuscated_result = std_obfuscator.hex_encode(base_payload.strip('; '))
                        elif args.encode == 'unicode':
                            obfuscated_result = std_obfuscator.unicode_encode(base_payload)
                    
                    elif args.obfuscate:
                        if args.obfuscate == 'quote':
                            obfuscated_result = std_obfuscator.quote_injection(base_payload.strip('; '))
                        elif args.obfuscate == 'backslash':
                            obfuscated_result = std_obfuscator.backslash_escape(base_payload.strip('; '))
                        elif args.obfuscate == 'variable':
                            obfuscated_result = std_obfuscator.variable_expansion(base_payload.strip('; '))
                        elif args.obfuscate == 'ifs':
                            obfuscated_result = std_obfuscator.space_to_ifs(base_payload)
                        elif args.obfuscate == 'wildcard':
                            obfuscated_result = std_obfuscator.wildcard_path(base_payload)
                        elif args.obfuscate == 'case' and os_type == 'windows':
                            obfuscated_result = std_obfuscator.case_variation(base_payload)
                        elif args.obfuscate == 'brace':
                            obfuscated_result = std_obfuscator.space_to_brace(base_payload)
                    
                    elif args.preset:
                        preset = get_preset(args.preset)
                        obfuscated_result = std_obfuscator.chain_techniques(base_payload, preset['techniques'])
                    
                    # Apply advanced obfuscation
                    elif args.advanced and args.technique:
                        cmd_parts = base_payload.strip('; ').split(' ', 1)
                        command = cmd_parts[0]
                        arguments = cmd_parts[1] if len(cmd_parts) > 1 else ''
                        
                        if args.technique == 'brace':
                            if args.complexity == 1:
                                obfuscated_result = adv_obfuscator.brace_expand_basic(command, arguments)
                            elif args.complexity == 2:
                                obfuscated_result = adv_obfuscator.brace_expand_nested(command, arguments)
                            elif args.complexity == 4:
                                obfuscated_result = adv_obfuscator.brace_expand_wildcard_combo(command, arguments if arguments else '/etc/passwd')
                            else:
                                obfuscated_result = adv_obfuscator.brace_expand_basic(command, arguments)
                        
                        elif args.technique == 'reverse':
                            if args.complexity == 1:
                                obfuscated_result = adv_obfuscator.reverse_with_rev(base_payload.strip('; '))
                            elif args.complexity == 2:
                                obfuscated_result = adv_obfuscator.reverse_with_parameter_expansion(base_payload.strip('; '))
                            elif args.complexity == 3:
                                obfuscated_result = adv_obfuscator.reverse_char_by_char(command)
                            elif args.complexity >= 4:
                                obfuscated_result = adv_obfuscator.reverse_base64_combo(base_payload.strip('; '))
                        
                        elif args.technique == 'arithmetic':
                            if args.complexity == 1:
                                obfuscated_result = adv_obfuscator.ascii_to_char_basic(command)
                            elif args.complexity == 2:
                                obfuscated_result = adv_obfuscator.ascii_to_char_octal(command)
                            elif args.complexity == 3:
                                obfuscated_result = adv_obfuscator.ascii_arithmetic_nested(command)
                            elif args.complexity >= 4:
                                obfuscated_result = adv_obfuscator.ascii_bitwise_construction(command)
                    
                    # Add obfuscation to result
                    if obfuscated_result:
                        result['obfuscation'] = obfuscated_result
                    
                    # Analyze payload
                    payload_to_analyze = base_payload
                    if obfuscated_result and 'obfuscated' in obfuscated_result:
                        payload_to_analyze = obfuscated_result['obfuscated']
                    elif obfuscated_result and 'final_payload' in obfuscated_result:
                        payload_to_analyze = obfuscated_result['final_payload']
                    
                    analysis = analyze_payload(payload_to_analyze)
                    result['analysis'] = analysis
                    
                    all_payloads.append(result)
                    
                    # CLI output
                    if args.output in ['cli', 'all']:
                        print(format_payload_output(
                            payload_info, 
                            obfuscated_result, 
                            analysis, 
                            args.explain
                        ))
    
    # JSON output
    if args.output in ['json', 'all']:
        json_file = args.file if args.file else 'payloads.json'
        generate_json_output(all_payloads, json_file)
    
    # Text catalog output
    if args.output in ['txt', 'all']:
        txt_file = args.file if args.file and args.output == 'txt' else 'payloads_catalog.txt'
        generate_txt_catalog(all_payloads, txt_file)
    
    # Defense recommendations
    if args.defense:
        print(f"\n{Colors.BOLD}[DEFENSIVE RECOMMENDATIONS]{Colors.ENDC}")
        print(DEFENSE_SUMMARY)
    
    # Summary
    print(f"\n{Colors.GREEN}[✓] Generated {len(all_payloads)} payload templates{Colors.ENDC}")
    print(f"{Colors.YELLOW}[⚠️ ] Remember: For authorized testing only!{Colors.ENDC}\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}[!] Operation cancelled by user{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[✗] Error: {str(e)}{Colors.ENDC}")
        sys.exit(1)
