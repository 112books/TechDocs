#!/bin/bash
# TechDocs PDF Generator - Simple and robust
# Usage: ./scripts/generate-pdf.sh <input.md> [output.pdf]

set -euo pipefail

INPUT="${1:-}"
OUTPUT="${2:-}"

# Validate input
if [ -z "$INPUT" ]; then
  echo "Error: No input file specified"
  echo "Usage: $0 <input.md> [output.pdf]"
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Error: File '$INPUT' not found"
  exit 1
fi

# Default output name
if [ -z "$OUTPUT" ]; then
  OUTPUT="${INPUT%.md}.pdf"
fi

# Extract metadata (simple and safe)
TITLE=$(grep -m1 '^title:' "$INPUT" | sed 's/^title: *"*\([^"]*\)"*/\1/' || echo "Untitled")
REVISION=$(grep -m1 '^revision:' "$INPUT" | sed 's/^revision: *"*\([^"]*\)"*/\1/' || echo "1.0")
APPROVED_BY=$(grep -m1 '^approved_by:' "$INPUT" | sed 's/^approved_by: *"*\([^"]*\)"*/\1/' || echo "N/A")
APPROVED_DATE=$(grep -m1 '^approved_date:' "$INPUT" | sed 's/^approved_date: *"*\([^"]*\)"*/\1/' || echo "N/A")

echo "Generating PDF..."
echo "  Title: $TITLE"
echo "  Revision: $REVISION"
echo "  Approved by: $APPROVED_BY"
echo "  Date: $APPROVED_DATE"

# Try WeasyPrint first
if command -v weasyprint &>/dev/null; then
  pandoc "$INPUT" \
    --pdf-engine=weasyprint \
    -V paper-size=A4 \
    -V margin-top=2cm \
    -V margin-bottom=2cm \
    -V margin-left=2cm \
    -V margin-right=2cm \
    -V title="$TITLE" \
    -V revision="$REVISION" \
    -V approved-by="$APPROVED_BY" \
    -V approved-date="$APPROVED_DATE" \
    --metadata-file=config/pandoc-metadata.yaml \
    -o "$OUTPUT"
  echo "✓ PDF generated: $OUTPUT"
else
  echo "⚠ WeasyPrint not found"
  # Fallback to HTML
  HTML_OUT="${OUTPUT%.pdf}.html"
  pandoc "$INPUT" -s -o "$HTML_OUT" --metadata title="$TITLE"
  echo "Generated HTML: $HTML_OUT"
fi
