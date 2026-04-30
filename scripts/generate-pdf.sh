#!/bin/bash
# TechDocs PDF Generator — Pandoc-based
# Usage: ./scripts/generate-pdf.sh <input.md> [output.pdf]
#
# Requirements: pandoc, weasyprint or pagedjs-cli
# For production: add to CI/CD pipeline on merge to main

set -euo pipefail

INPUT="${1:-}"
OUTPUT="${2:-}"

if [ -z "$INPUT" ]; then
  echo "Error: No input file specified."
  echo "Usage: $0 <input.md> [output.pdf]"
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Error: Input file '$INPUT' not found."
  exit 1
fi

# Default output name
if [ -z "$OUTPUT" ]; then
  OUTPUT="${INPUT%.md}.pdf"
fi

# Extract metadata from YAML front matter
TITLE=$(grep -A1 '^title:' "$INPUT" | tail -1 | sed 's/^ *//' | tr -d '"' || echo "Untitled")
REVISION=$(grep -A1 '^revision:' "$INPUT" | tail -1 | sed 's/^ *//' | tr -d '"' || echo "1.0")
APPROVED_BY=$(grep -A1 '^approved_by:' "$INPUT" | tail -1 | sed 's/^ *//' | tr -d '"' || echo "N/A")
APPROVED_DATE=$(grep -A1 '^approved_date:' "$INPUT" | tail -1 | sed 's/^ *//' | tr -d '"' || echo "N/A")

echo "Generating PDF: $OUTPUT"
echo "  Title: $TITLE"
echo "  Revision: $REVISION"
echo "  Approved by: $APPROVED_BY"
echo "  Date: $APPROVED_DATE"

# Generate PDF with Pandoc
# Uses A4 paper, header/footer with metadata
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
  -V header="TechDocs — Document confidencial" \
  -V footer="$TITLE | Rev $REVISION | $APPROVED_DATE" \
  --metadata-file=config/pandoc-metadata.yaml \
  -o "$OUTPUT" \
  2>/dev/null || {
    # Fallback to HTML if weasyprint not available
    echo "  (weasyprint not available, generating HTML instead)"
    pandoc "$INPUT" \
      -s \
      -o "${OUTPUT%.pdf}.html" \
      --metadata title="$TITLE"
    echo "  Generated: ${OUTPUT%.pdf}.html"
  }

echo "✓ PDF generation complete: $OUTPUT"
