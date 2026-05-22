#!/usr/bin/env python3
"""Markdown to PDF converter using markdown + weasyprint."""

import sys
import markdown
from weasyprint import HTML

STYLE = """
@page { size: A4; margin: 2cm }
body { font-family: Arial, Helvetica, sans-serif; line-height: 1.6; color: #1E293B }
h1 { font-size: 24pt; color: #1B2A4A; border-bottom: 3px solid #1B2A4A; padding-bottom: 8pt; margin-top: 24pt }
h2 { font-size: 18pt; color: #2563EB; margin-top: 20pt; border-bottom: 1px solid #E2E8F0; padding-bottom: 4pt }
h3 { font-size: 14pt; color: #1E293B; margin-top: 16pt }
table { width: 100%; border-collapse: collapse; margin: 12pt 0 }
th { background: #1B2A4A; color: white; padding: 8pt; text-align: left; font-weight: bold }
td { padding: 6pt 8pt; border-bottom: 1px solid #E2E8F0 }
tr:nth-child(even) { background: #F8F9FA }
code { background: #EFF6FF; padding: 2pt 6pt; border-radius: 3pt; font-size: 9pt }
pre { background: #F8F9FA; padding: 12pt; border-radius: 4pt; overflow: auto; font-size: 9pt }
blockquote { border-left: 4px solid #2563EB; padding-left: 12pt; color: #64748B }
hr { border: none; border-top: 2px solid #E2E8F0; margin: 16pt 0 }
p { margin: 8pt 0 }
ul, ol { padding-left: 24pt }
li { margin: 4pt 0 }
"""

def md_to_pdf(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        # Skip frontmatter
        content = f.read()
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                content = content[end + 3:].strip()
    
    html_body = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    full_html = f'<html><head><meta charset="utf-8"></head><body>{html_body}</body></html>'
    
    from weasyprint import HTML, CSS
    html_obj = HTML(string=full_html)
    css_obj = CSS(string=STYLE)
    html_obj.write_pdf(output_file, stylesheets=[css_obj])
    print(f"PDF generated: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: md2pdf.py <input.md> [output.pdf]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.md', '.pdf')
    md_to_pdf(input_file, output_file)
