#!/usr/bin/env python3
# run_sqli.py

import argparse
from sqli_generator import SQLiGenerator

def main():
    parser = argparse.ArgumentParser(description="SQLi Payload Generator (Standalone)")
    parser.add_argument('--db', choices=['mysql', 'postgresql', 'mssql', 'all'], default='all',
                        help='Database type')
    parser.add_argument('--type', choices=['error', 'union', 'blind', 'comment_bypass', 'case_variation', 'all'], default='all',
                        help='Injection type')
    parser.add_argument('--encode', choices=['url', 'base64', 'hex', 'none'], default='none',
                        help='Apply encoding')
    parser.add_argument('--obfuscate', action='store_true', help='Apply obfuscation')
    parser.add_argument('--output', choices=['terminal', 'json', 'txt', 'burp', 'zap', 'all'],
                        default='terminal', help='Output format')
    parser.add_argument('--filename', default=None, help='Custom filename (without extension)')

    args = parser.parse_args()

    gen = SQLiGenerator(db=args.db, injection_type=args.type, 
                        encode=args.encode if args.encode != 'none' else None,
                        obfuscate=args.obfuscate)
    gen.output(args.output, args.filename)

if __name__ == '__main__':
    main()