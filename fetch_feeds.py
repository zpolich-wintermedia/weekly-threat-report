import markdown
import pdfkit
import re
from datetime import datetime
import os
import pathlib

# === Logo Setup ===
logo_filename = "logo.png"
logo_path = pathlib.Path(logo_filename).resolve()
logo_uri = logo_path.as_uri()

if not logo_path.is_file():
    raise FileNotFoundError(f"Logo file not found at: {logo_path}")

# === Load and clean markdown ===
with open("weekly_threat_report.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Remove first-level markdown title if present
if lines and lines[0].strip().startswith("#"):
    lines = lines[1:]

clean_md = "".join(lines)

# === Highlight MITRE Techniques ===
def style_mitre_tags(md_text):
    return re.sub(r"\b(T\d{4}(?:\.\d{3})?)\b", r'<span class="mitre">\1</span>', md_text)

styled_md = style_mitre_tags(clean_md)
html_body = markdown.markdown(styled_md)

# === Cover page content ===
report_date = datetime.now().strftime("%B %d, %Y")
cover_html = f"""
<div class="cover">
<img src="{logo_uri}" alt="Company Logo" style="width:200px; display:block; margin: 0 auto 40px auto;">
<h1>Weekly Threat Report</h1>
<p class="meta">Date: {report_date}</p>
<p class="meta">Prepared by: TechCXO Security Team</p>
</div>
<div class="page-break"></div>
"""

# === Final HTML document ===
full_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Weekly Threat Report</title>
<style>
@page {{
size: A4;
margin: 30mm 20mm 20mm 20mm;
@top-left {{
content: url("{logo_uri}");
vertical-align: middle;
margin: 10px;
}}
@bottom-center {{
content: "Page " counter(page);
font-size: 10px;
color: #555;
}}
}}
body {{
font-family: "Segoe UI", Tahoma, sans-serif;
margin: 40px;
color: #2b2b2b;
line-height: 1.6;
}}
h1 {{
text-align: center;
font-size: 28px;
border-bottom: 2px solid #333;
padding-bottom: 5px;
}}
h2 {{
color: #003366;
margin-top: 30px;
}}
a {{
color: #1a0dab;
text-decoration: none;
}}
.meta {{
font-size: 14px;
color: #555;
text-align: center;
}}
.cover {{
margin-top: 200px;
}}
.page-break {{
page-break-after: always;
}}
.mitre {{
display: inline-block;
background-color: #f0f0f0;
padding: 4px 8px;
margin: 3px 3px 3px 0;
font-size: 12px;
font-weight: bold;
border: 1px solid #ccc;
border-radius: 4px;
color: #333;
}}
</style>
</head>
<body>
{cover_html}
{html_body}
</body>
</html>
"""

# === Output PDF location ===
output_file = os.path.join(
    r"C:\Users\zacha\OneDrive\Documents\Reports\ThreatReports",
    f"weekly_threat_report_{datetime.now().strftime('%Y-%m-%d')}.pdf"
)

# === wkhtmltopdf Configuration ===
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

# === PDF Generation ===
pdfkit.from_string(
    full_html,
    output_file,
    configuration=config,
    options={"enable-local-file-access": ""}
)

print(f"✅ PDF created: {output_file}")
