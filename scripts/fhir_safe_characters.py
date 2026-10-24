#!/usr/bin/env python3
"""
FHIR Server-Safe Character Replacement Script

Identifies and replaces non-standard Unicode characters (em-dashes, smart quotes,
non-breaking spaces, etc.) with their ASCII equivalents for FHIR server compatibility.
"""

import json
import re
import sys
from pathlib import Path

# Mapping of problematic Unicode characters to FHIR-safe ASCII equivalents
CHAR_REPLACEMENTS = {
    # Dashes
    '\u2014': '-',  # Em dash (—)
    '\u2013': '-',  # En dash (–)
    '\u2012': '-',  # Figure dash (‒)
    '\u2015': '-',  # Horizontal bar (―)
    '\u2010': '-',  # Hyphen (‐)
    '\u2011': '-',  # Non-breaking hyphen (‑)
    '\u00AD': '-',  # Soft hyphen (­)

    # Quotes
    '\u2018': "'",  # Left single quote (')
    '\u2019': "'",  # Right single quote (')
    '\u201A': "'",  # Single low-9 quote (‚)
    '\u201B': "'",  # Single high-reversed-9 quote (‛)
    '\u2032': "'",  # Prime (′)
    '\u2035': "'",  # Reversed prime (‵)
    '\u201C': '"',  # Left double quote (")
    '\u201D': '"',  # Right double quote (")
    '\u201E': '"',  # Double low-9 quote („)
    '\u201F': '"',  # Double high-reversed-9 quote (‟)
    '\u2033': '"',  # Double prime (″)
    '\u2036': '"',  # Reversed double prime (‶)
    '\u00AB': '"',  # Left guillemet («)
    '\u00BB': '"',  # Right guillemet (»)
    '\u2039': "'",  # Single left guillemet (‹)
    '\u203A': "'",  # Single right guillemet (›)

    # Spaces
    '\u00A0': ' ',  # Non-breaking space
    '\u2002': ' ',  # En space
    '\u2003': ' ',  # Em space
    '\u2004': ' ',  # Three-per-em space
    '\u2005': ' ',  # Four-per-em space
    '\u2006': ' ',  # Six-per-em space
    '\u2007': ' ',  # Figure space
    '\u2008': ' ',  # Punctuation space
    '\u2009': ' ',  # Thin space
    '\u200A': ' ',  # Hair space
    '\u200B': '',   # Zero-width space (remove)
    '\u202F': ' ',  # Narrow no-break space
    '\u205F': ' ',  # Medium mathematical space
    '\u3000': ' ',  # Ideographic space
    '\uFEFF': '',   # BOM / Zero-width no-break space (remove)

    # Ellipsis
    '\u2026': '...',  # Horizontal ellipsis (…)

    # Bullets and symbols
    '\u2022': '*',  # Bullet (•)
    '\u2023': '>',  # Triangular bullet (‣)
    '\u2043': '-',  # Hyphen bullet (⁃)
    '\u25E6': 'o',  # White bullet (◦)
    '\u00B7': '.',  # Middle dot (·)

    # Scientific notation / units
    '\u00B5': 'u',         # Micro sign (µ) -> u (e.g., umol/L)
    '\u03BC': 'u',         # Greek small letter mu (μ) -> u
    '\u00B2': '2',         # Superscript two (²)
    '\u00B3': '3',         # Superscript three (³)
    '\u00B9': '1',         # Superscript one (¹)
    '\u2070': '0',         # Superscript zero (⁰)
    '\u2074': '4',         # Superscript four (⁴)
    '\u2075': '5',         # Superscript five (⁵)
    '\u2076': '6',         # Superscript six (⁶)
    '\u2077': '7',         # Superscript seven (⁷)
    '\u2078': '8',         # Superscript eight (⁸)
    '\u2079': '9',         # Superscript nine (⁹)

    # Other common problematic characters
    '\u00B0': ' degrees',  # Degree symbol (°) - or use 'deg'
    '\u00B1': '+/-',       # Plus-minus (±)
    '\u00D7': 'x',         # Multiplication sign (×)
    '\u00F7': '/',         # Division sign (÷)
    '\u2260': '!=',        # Not equal (≠)
    '\u2264': '<=',        # Less than or equal (≤)
    '\u2265': '>=',        # Greater than or equal (≥)
    '\u00AE': '(R)',       # Registered trademark (®)
    '\u2122': '(TM)',      # Trademark (™)
    '\u00A9': '(C)',       # Copyright (©)
    '\u00BC': '1/4',       # Vulgar fraction 1/4 (¼)
    '\u00BD': '1/2',       # Vulgar fraction 1/2 (½)
    '\u00BE': '3/4',       # Vulgar fraction 3/4 (¾)
}


def find_non_ascii_characters(text: str) -> list[tuple[int, str, str, int]]:
    """
    Find all non-ASCII characters in text.

    Returns list of tuples: (position, character, unicode_name, codepoint)
    """
    import unicodedata
    findings = []
    for i, char in enumerate(text):
        if ord(char) > 127:
            try:
                name = unicodedata.name(char, 'UNKNOWN')
            except ValueError:
                name = 'UNKNOWN'
            findings.append((i, char, name, ord(char)))
    return findings


def replace_non_standard_chars(text: str, report: bool = False) -> tuple[str, list[dict]]:
    """
    Replace non-standard characters with FHIR-safe equivalents.

    Args:
        text: Input text to process
        report: If True, generate a report of replacements

    Returns:
        Tuple of (cleaned_text, list of replacement reports)
    """
    replacements_made = []
    result = text

    for char, replacement in CHAR_REPLACEMENTS.items():
        if char in result:
            count = result.count(char)
            if report and count > 0:
                replacements_made.append({
                    'character': char,
                    'codepoint': f'U+{ord(char):04X}',
                    'replacement': replacement if replacement else '(removed)',
                    'count': count
                })
            result = result.replace(char, replacement)

    return result, replacements_made


def process_json_file(filepath: Path, output_path: Path = None, dry_run: bool = False) -> dict:
    """
    Process a JSON file and replace non-standard characters.

    Args:
        filepath: Path to input JSON file
        output_path: Path for output file (optional, defaults to overwriting input)
        dry_run: If True, only report findings without making changes

    Returns:
        Report dictionary with findings and replacements
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all non-ASCII characters first
    findings = find_non_ascii_characters(content)

    # Replace non-standard characters
    cleaned_content, replacements = replace_non_standard_chars(content, report=True)

    report = {
        'file': str(filepath),
        'total_non_ascii_found': len(findings),
        'unique_characters': len(set(f[1] for f in findings)),
        'replacements_made': replacements,
        'non_standard_remaining': []
    }

    # Check for remaining non-ASCII characters not in our replacement map
    remaining = find_non_ascii_characters(cleaned_content)
    if remaining:
        report['non_standard_remaining'] = [
            {
                'character': char,
                'codepoint': f'U+{cp:04X}',
                'name': name,
                'positions': [pos]
            }
            for pos, char, name, cp in remaining
        ]

    if not dry_run:
        out_path = output_path or filepath
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        report['output_file'] = str(out_path)

    return report


def process_text(text: str) -> tuple[str, dict]:
    """
    Process a text string and return cleaned version with report.
    """
    findings = find_non_ascii_characters(text)
    cleaned, replacements = replace_non_standard_chars(text, report=True)

    report = {
        'total_non_ascii_found': len(findings),
        'replacements_made': replacements,
    }

    return cleaned, report


def scan_directory(directory: Path, pattern: str = "*.json", dry_run: bool = True) -> list[dict]:
    """
    Scan a directory for files with non-standard characters.

    Args:
        directory: Directory to scan
        pattern: Glob pattern for files to check
        dry_run: If True, only report without making changes

    Returns:
        List of reports for files with issues
    """
    reports = []
    for filepath in directory.rglob(pattern):
        try:
            report = process_json_file(filepath, dry_run=dry_run)
            if report['replacements_made'] or report['non_standard_remaining']:
                reports.append(report)
        except Exception as e:
            reports.append({
                'file': str(filepath),
                'error': str(e)
            })
    return reports


def print_report(report: dict):
    """Pretty print a processing report."""
    print(f"\n{'='*60}")
    print(f"File: {report.get('file', 'N/A')}")
    print(f"{'='*60}")

    if 'error' in report:
        print(f"ERROR: {report['error']}")
        return

    print(f"Total non-ASCII characters found: {report['total_non_ascii_found']}")

    if report['replacements_made']:
        print("\nReplacements made:")
        for r in report['replacements_made']:
            # Use ASCII-safe printing for Windows console compatibility
            char_repr = r['character'].encode('unicode_escape').decode('ascii')
            print(f"  {char_repr} ({r['codepoint']}) -> '{r['replacement']}' (x{r['count']})")

    if report.get('non_standard_remaining'):
        print("\nWARNING: Non-standard characters remaining (not in replacement map):")
        for r in report['non_standard_remaining']:
            char_repr = r['character'].encode('unicode_escape').decode('ascii')
            print(f"  {char_repr} ({r['codepoint']}) - {r['name']}")

    if 'output_file' in report:
        print(f"\nOutput written to: {report['output_file']}")


# Example usage and CLI
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Make text/JSON files FHIR server-safe by replacing non-standard characters'
    )
    parser.add_argument('input', nargs='?', help='Input file or directory path')
    parser.add_argument('-o', '--output', help='Output file path (default: overwrite input)')
    parser.add_argument('-d', '--directory', action='store_true',
                        help='Process all JSON files in directory recursively')
    parser.add_argument('-n', '--dry-run', action='store_true',
                        help='Only report issues without making changes')
    parser.add_argument('-p', '--pattern', default='*.*',
                        help='File pattern for directory mode (default: *.*). Use *.json, *.fsh, etc.')
    parser.add_argument('--demo', action='store_true',
                        help='Run a demonstration with sample text')

    args = parser.parse_args()

    if args.demo or not args.input:
        # Demo mode
        sample_text = '''
        This text contains "smart quotes" and 'apostrophes'.
        It also has an em-dash — and an en-dash – for good measure.
        Don't forget the ellipsis… and non-breaking spaces here.
        Some math: 2 × 3 = 6, and 10 ÷ 2 = 5.
        Temperature is 98.6° Fahrenheit.
        '''

        print("FHIR Safe Character Replacement Demo")
        print("="*60)
        print("\nOriginal text:")
        print(sample_text)

        cleaned, report = process_text(sample_text)

        print("\nCleaned text:")
        print(cleaned)

        print("\nReplacements made:")
        for r in report['replacements_made']:
            print(f"  {r['character']} ({r['codepoint']}) -> '{r['replacement']}' (x{r['count']})")

        if not args.input:
            print("\n" + "-"*60)
            print("Usage: python fhir_safe_characters.py <file_or_directory> [options]")
            print("       python fhir_safe_characters.py --help for more options")

    elif args.directory:
        directory = Path(args.input)
        if not directory.is_dir():
            print(f"Error: {args.input} is not a directory")
            sys.exit(1)

        reports = scan_directory(directory, pattern=args.pattern, dry_run=args.dry_run)

        if not reports:
            print("No files with non-standard characters found.")
        else:
            for report in reports:
                print_report(report)

            print(f"\n{'='*60}")
            print(f"Total files with issues: {len(reports)}")
            if args.dry_run:
                print("(Dry run - no changes made. Remove --dry-run to apply fixes)")

    else:
        filepath = Path(args.input)
        if not filepath.exists():
            print(f"Error: {args.input} does not exist")
            sys.exit(1)

        output_path = Path(args.output) if args.output else None
        report = process_json_file(filepath, output_path, dry_run=args.dry_run)
        print_report(report)

        if args.dry_run:
            print("\n(Dry run - no changes made. Remove --dry-run to apply fixes)")
