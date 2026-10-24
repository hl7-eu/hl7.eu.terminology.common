#!/usr/bin/env python3
"""
UTF-8 Encoding Fixer Script

Ensures files are properly UTF-8 encoded with correct Unicode characters.
Fixes mojibake (badly encoded characters) and normalizes to UTF-8.
Does NOT replace special characters - keeps em-dashes, micro signs, etc.
"""

import sys
import unicodedata
from pathlib import Path

# Common mojibake patterns: what they look like -> what they should be
MOJIBAKE_FIXES = {
    # UTF-8 bytes misinterpreted as Windows-1252/Latin-1
    'â€"': '–',      # En dash
    'â€"': '—',      # Em dash
    'â€™': "'",      # Right single quote
    'â€œ': '"',      # Left double quote
    'â€�': '"',      # Right double quote (with replacement char)
    'â€¢': '•',      # Bullet
    'â€¦': '…',      # Ellipsis
    'Â°': '°',       # Degree
    'Âµ': 'µ',       # Micro
    'Ã—': '×',       # Multiplication
    'Ã·': '÷',       # Division
    'Â²': '²',       # Superscript 2
    'Â³': '³',       # Superscript 3
    'Â±': '±',       # Plus-minus
    'Ã¶': 'ö',       # o with diaeresis
    'Ã¼': 'ü',       # u with diaeresis
    'Ã©': 'é',       # e with acute
    'Ã¨': 'è',       # e with grave
    'Ã«': 'ë',       # e with diaeresis
    'Ã¸': 'ø',       # o with stroke
    'Ã¤': 'ä',       # a with diaeresis
    'Ã': 'Ä',       # A with diaeresis (partial)
    '\x00': '',      # Null bytes
    '\ufeff': '',    # BOM (remove)
}


def detect_encoding(file_path: Path) -> str:
    """Try to detect the file encoding."""
    encodings_to_try = ['utf-8', 'utf-8-sig', 'utf-16', 'cp1252', 'latin-1', 'iso-8859-1']

    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                f.read()
            return encoding
        except (UnicodeDecodeError, UnicodeError):
            continue

    return 'utf-8'  # Default fallback


def fix_mojibake(text: str) -> tuple[str, list[str]]:
    """Fix common mojibake patterns."""
    fixes_applied = []
    result = text

    for bad, good in MOJIBAKE_FIXES.items():
        if bad in result:
            count = result.count(bad)
            result = result.replace(bad, good)
            fixes_applied.append(f"'{bad}' -> '{good}' (x{count})")

    return result, fixes_applied


def normalize_unicode(text: str) -> str:
    """Normalize Unicode to NFC form (composed characters)."""
    return unicodedata.normalize('NFC', text)


def find_encoding_issues(text: str) -> list[dict]:
    """Find characters that might indicate encoding problems."""
    issues = []

    # Look for replacement character
    if '\ufffd' in text:
        issues.append({
            'character': '\ufffd',
            'name': 'REPLACEMENT CHARACTER',
            'count': text.count('\ufffd'),
            'note': 'Indicates failed character decoding'
        })

    # Look for C1 control characters (often indicate encoding issues)
    for i, char in enumerate(text):
        cp = ord(char)
        if 0x80 <= cp <= 0x9F:
            issues.append({
                'character': char,
                'codepoint': f'U+{cp:04X}',
                'position': i,
                'note': 'C1 control character - possible encoding issue'
            })

    return issues


def process_file(filepath: Path, output_path: Path = None, dry_run: bool = False) -> dict:
    """
    Process a file to fix encoding issues.

    Args:
        filepath: Path to input file
        output_path: Path for output file (optional)
        dry_run: If True, only report without making changes

    Returns:
        Report dictionary
    """
    # Detect and read with appropriate encoding
    detected_encoding = detect_encoding(filepath)

    with open(filepath, 'rb') as f:
        raw_bytes = f.read()

    # Try to decode
    try:
        content = raw_bytes.decode('utf-8')
        source_encoding = 'utf-8'
    except UnicodeDecodeError:
        try:
            content = raw_bytes.decode('utf-8-sig')
            source_encoding = 'utf-8-sig (with BOM)'
        except UnicodeDecodeError:
            content = raw_bytes.decode('cp1252', errors='replace')
            source_encoding = 'cp1252 (Windows)'

    report = {
        'file': str(filepath),
        'detected_encoding': source_encoding,
        'size_bytes': len(raw_bytes),
        'mojibake_fixes': [],
        'encoding_issues': [],
        'normalized': False
    }

    # Fix mojibake
    fixed_content, mojibake_fixes = fix_mojibake(content)
    report['mojibake_fixes'] = mojibake_fixes

    # Normalize Unicode
    normalized_content = normalize_unicode(fixed_content)
    if normalized_content != fixed_content:
        report['normalized'] = True

    # Check for remaining issues
    report['encoding_issues'] = find_encoding_issues(normalized_content)

    # Write output
    if not dry_run:
        out_path = output_path or filepath
        with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(normalized_content)
        report['output_file'] = str(out_path)
        report['output_encoding'] = 'utf-8'

    return report


def scan_for_special_chars(filepath: Path) -> dict:
    """Scan a file and report all non-ASCII characters found."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    char_counts = {}
    for char in content:
        if ord(char) > 127:
            if char not in char_counts:
                try:
                    name = unicodedata.name(char, 'UNKNOWN')
                except ValueError:
                    name = 'UNKNOWN'
                char_counts[char] = {
                    'char': char,
                    'codepoint': f'U+{ord(char):04X}',
                    'name': name,
                    'count': 0
                }
            char_counts[char]['count'] += 1

    return {
        'file': str(filepath),
        'total_non_ascii': sum(c['count'] for c in char_counts.values()),
        'unique_characters': len(char_counts),
        'characters': sorted(char_counts.values(), key=lambda x: -x['count'])
    }


def print_report(report: dict):
    """Pretty print a processing report."""
    print(f"\n{'='*60}")
    print(f"File: {report.get('file', 'N/A')}")
    print(f"{'='*60}")

    if 'detected_encoding' in report:
        print(f"Source encoding: {report['detected_encoding']}")
        print(f"File size: {report['size_bytes']:,} bytes")

    if report.get('mojibake_fixes'):
        print(f"\nMojibake fixes applied: {len(report['mojibake_fixes'])}")
        for fix in report['mojibake_fixes'][:10]:
            print(f"  {fix}")
        if len(report['mojibake_fixes']) > 10:
            print(f"  ... and {len(report['mojibake_fixes']) - 10} more")

    if report.get('normalized'):
        print("\nUnicode normalized to NFC form")

    if report.get('encoding_issues'):
        print(f"\nRemaining encoding issues: {len(report['encoding_issues'])}")
        for issue in report['encoding_issues'][:5]:
            print(f"  {issue}")

    if 'output_file' in report:
        print(f"\nOutput written to: {report['output_file']}")
        print(f"Output encoding: {report['output_encoding']}")

    # For scan reports
    if 'characters' in report:
        print(f"\nTotal non-ASCII characters: {report['total_non_ascii']:,}")
        print(f"Unique characters: {report['unique_characters']}")
        print("\nTop characters found:")
        for c in report['characters'][:20]:
            print(f"  {c['char']} ({c['codepoint']}) {c['name']}: {c['count']:,}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Fix file encoding issues and normalize to UTF-8'
    )
    parser.add_argument('input', nargs='?', help='Input file path')
    parser.add_argument('-o', '--output', help='Output file path (default: overwrite input)')
    parser.add_argument('-n', '--dry-run', action='store_true',
                        help='Only report issues without making changes')
    parser.add_argument('-s', '--scan', action='store_true',
                        help='Scan and report all non-ASCII characters')

    args = parser.parse_args()

    if not args.input:
        print("Usage: python fix_encoding.py <file> [options]")
        print("       python fix_encoding.py <file> --scan  # List all special characters")
        print("       python fix_encoding.py <file> --dry-run  # Check without changes")
        print("       python fix_encoding.py <file>  # Fix and save")
        sys.exit(0)

    filepath = Path(args.input)
    if not filepath.exists():
        print(f"Error: {args.input} does not exist")
        sys.exit(1)

    if args.scan:
        report = scan_for_special_chars(filepath)
    else:
        output_path = Path(args.output) if args.output else None
        report = process_file(filepath, output_path, dry_run=args.dry_run)

    print_report(report)
