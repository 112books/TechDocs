#!/usr/bin/env python3
"""
TechDocs Pipeline — Bloc → Document → Export

Usage:
    python build.py --manual seco-sv1003 --lang ca --format html
    python build.py --manual seco-sv1003 --lang ca --format json
    python build.py --list-blocks
    python build.py --list-compositions
    python build.py --check-translations --lang es
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# --- Config ---
VAULT_DIR = Path(__file__).parent.parent / "vault"
BLOCKS_DIR = VAULT_DIR / "blocks"
COMPOSITIONS_DIR = VAULT_DIR / "compositions"
EXPORTS_DIR = VAULT_DIR.parent / "exports"

BLOCK_TYPES = ["warning", "procedure", "specification", "legal", "definition", "reference"]

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    fm_text = match.group(1)
    body = match.group(2)
    fm = {}
    current_key = None
    current_list = None
    
    for line in fm_text.split('\n'):
        # Check for list item
        if line.startswith('  - ') and current_key:
            value = line.strip()[2:].strip().strip('"').strip("'")
            if current_list is not None:
                current_list.append(value)
            continue
        
        # Check for key: value
        if ':' in line and not line.startswith(' '):
            # Save previous list if any
            if current_key and current_list is not None:
                fm[current_key] = current_list
                current_list = None
            
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip()
            current_key = key
            
            # Empty value might be a list that follows
            if not value:
                current_list = []
                continue
            # Parse inline arrays
            if value.startswith('[') and value.endswith(']'):
                items = value[1:-1].split(',')
                fm[key] = [item.strip().strip('"').strip("'") for item in items if item.strip()]
                current_key = None
            # Parse booleans
            elif value.lower() == 'true':
                fm[key] = True
                current_key = None
            elif value.lower() == 'false':
                fm[key] = False
                current_key = None
            # Parse integers
            elif value.isdigit():
                fm[key] = int(value)
                current_key = None
            # Parse strings (strip quotes)
            else:
                fm[key] = value.strip('"').strip("'")
                current_key = None
    
    # Save last list if any
    if current_key and current_list is not None:
        fm[current_key] = current_list
    
    return fm, body

def load_block(block_id: str, language: str = "ca") -> tuple[dict, str] | None:
    """Load a block by ID and language."""
    for block_type in BLOCK_TYPES:
        pattern = f"{block_id}.{language}.md"
        filepath = BLOCKS_DIR / block_type / pattern
        if filepath.exists():
            content = filepath.read_text(encoding='utf-8')
            fm, body = parse_frontmatter(content)
            return fm, body
    return None

def load_composition(manual: str, chapter: str = None, language: str = "ca") -> list[tuple[dict, str, str]]:
    """Load a composition and resolve all block references."""
    composition_file = COMPOSITIONS_DIR / "manuals" / manual / f"{chapter}.{language}.md"
    if not composition_file.exists():
        print(f"ERROR: Composition not found: {composition_file}", file=sys.stderr)
        return []
    
    content = composition_file.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)
    
    blocks = fm.get('blocks', [])
    resolved = []
    for block_id in blocks:
        result = load_block(block_id, language)
        if result:
            block_fm, block_body = result
            resolved.append((block_id, block_fm, block_body))
        else:
            print(f"WARNING: Block {block_id} not found for language {language}", file=sys.stderr)
    
    return fm, resolved, body

def export_json(manual: str, language: str = "ca"):
    """Export a manual as JSON."""
    manual_dir = COMPOSITIONS_DIR / "manuals" / manual
    if not manual_dir.exists():
        print(f"ERROR: Manual not found: {manual}", file=sys.stderr)
        return
    
    output = {
        "manual": manual,
        "language": language,
        "generated": datetime.now().isoformat(),
        "chapters": []
    }
    
    for comp_file in sorted(manual_dir.glob(f"*.{language}.md")):
        # Extract chapter name without language suffix
        chapter_name = comp_file.name.replace(f".{language}.md", "")
        result = load_composition(manual, chapter_name, language)
        if not result:
            continue
        chapter_fm, blocks, chapter_body = result
        chapter_data = {
            "title": chapter_fm.get("title", chapter_name),
            "chapter": chapter_fm.get("chapter"),
            "weight": chapter_fm.get("weight"),
            "blocks": []
        }
        for block_id, block_fm, block_body in blocks:
            chapter_data["blocks"].append({
                "block_id": block_id,
                "type": block_fm.get("block_type"),
                "category": block_fm.get("block_category"),
                "title": block_fm.get("title"),
                "severity": block_fm.get("severity"),
                "tags": block_fm.get("tags", []),
                "applies_to": block_fm.get("applies_to", []),
                "content": block_body.strip()
            })
        output["chapters"].append(chapter_data)
    
    # Write
    export_dir = EXPORTS_DIR / "json"
    export_dir.mkdir(parents=True, exist_ok=True)
    output_file = export_dir / f"{manual}.{language}.json"
    output_file.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"JSON exported: {output_file}")

def list_blocks():
    """List all blocks in the vault."""
    blocks = []
    for block_type in BLOCK_TYPES:
        type_dir = BLOCKS_DIR / block_type
        if not type_dir.exists():
            continue
        for f in sorted(type_dir.glob("*.md")):
            content = f.read_text(encoding='utf-8')
            fm, _ = parse_frontmatter(content)
            blocks.append({
                "file": f.name,
                "block_id": fm.get("block_id", "?"),
                "type": fm.get("block_type", block_type),
                "language": fm.get("language", "?"),
                "title": fm.get("title", ""),
                "status": fm.get("status", "draft")
            })
    print(f"{'ID':<25} {'Type':<12} {'Lang':<4} {'Status':<10} Title")
    print("-" * 80)
    for b in blocks:
        print(f"{b['block_id']:<25} {b['type']:<12} {b['language']:<4} {b['status']:<10} {b['title']}")
    print(f"\nTotal: {len(blocks)} blocks")

def list_compositions():
    """List all compositions."""
    manuals_dir = COMPOSITIONS_DIR / "manuals"
    if not manuals_dir.exists():
        print("No compositions found.")
        return
    for manual_dir in sorted(manuals_dir.iterdir()):
        if not manual_dir.is_dir():
            continue
        files = list(manual_dir.glob("*.md"))
        print(f"\n{manual_dir.name}: {len(files)} compositions")
        for f in sorted(files):
            content = f.read_text(encoding='utf-8')
            fm, _ = parse_frontmatter(content)
            blocks = fm.get('blocks', [])
            print(f"  {f.stem} ({fm.get('language', '?')}) — {len(blocks)} blocks")

def check_translations(target_lang: str):
    """Check translation coverage for a target language."""
    # Find all blocks in source language (ca)
    source_blocks = set()
    for block_type in BLOCK_TYPES:
        type_dir = BLOCKS_DIR / block_type
        if not type_dir.exists():
            continue
        for f in type_dir.glob("*.ca.md"):
            content = f.read_text(encoding='utf-8')
            fm, _ = parse_frontmatter(content)
            source_blocks.add(fm.get("block_id", ""))
    
    # Find all blocks in target language
    translated_ids = set()
    for block_type in BLOCK_TYPES:
        type_dir = BLOCKS_DIR / block_type
        if not type_dir.exists():
            continue
        for f in type_dir.glob(f"*.{target_lang}.md"):
            content = f.read_text(encoding='utf-8')
            fm, _ = parse_frontmatter(content)
            translated_ids.add(fm.get("block_id", ""))
    
    # Compare
    missing = source_blocks - translated_ids
    coverage = len(translated_ids) / len(source_blocks) * 100 if source_blocks else 0
    print(f"Translation coverage for '{target_lang}':")
    print(f"  Source blocks (ca): {len(source_blocks)}")
    print(f"  Translated: {len(translated_ids)} ({coverage:.0f}%)")
    print(f"  Missing: {len(missing)}")
    if missing:
        print(f"  Missing blocks: {', '.join(sorted(missing))}")

def main():
    parser = argparse.ArgumentParser(description="TechDocs Pipeline")
    parser.add_argument("--manual", help="Manual slug (e.g. seco-sv1003)")
    parser.add_argument("--lang", default="ca", help="Language code (default: ca)")
    parser.add_argument("--format", choices=["json", "html", "pdf"], help="Export format")
    parser.add_argument("--list-blocks", action="store_true", help="List all blocks")
    parser.add_argument("--list-compositions", action="store_true", help="List all compositions")
    parser.add_argument("--check-translations", metavar="LANG", help="Check translation coverage")
    
    args = parser.parse_args()
    
    if args.list_blocks:
        list_blocks()
    elif args.list_compositions:
        list_compositions()
    elif args.check_translations:
        check_translations(args.check_translations)
    elif args.manual and args.format:
        if args.format == "json":
            export_json(args.manual, args.lang)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
