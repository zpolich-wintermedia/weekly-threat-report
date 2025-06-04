import os
import traceback
from fetch_feeds import fetch_articles, get_full_article
from summarize import generate_bluf_and_mitre
from report_generator import generate_markdown
import markdown
import pdfkit
import re
from datetime import datetime
import pathlib

print("📌 Running Weekly Threat Report script...")

try:
    # === STEP 1: Fetch + Summarize Articles ===
    articles = fetch_articles()
    for article in articles:
        full_text = get_full_article(article['link'])
        bluf, mitre_tags = generate_bluf_and_mitre(full_text)
        article['bluf'] = bluf
        article['mitre'] = mitre_tags

    # === STEP 2: Generate Markdown ===
    markdown_text = generate_markdown(articles)
    with open("weekly_threat_report.md", "w", encoding="utf-8") as f:
        f.write(markdown_text)
    print("✅ Markdown report generated.")

    # === STEP 3: Convert Markdown to PDF ===

    # Logo handling
    logo_filename = "logo.png"
    logo_path = pathlib.Path(logo_filename).resolve()
    logo_uri = logo_path.as_uri()

    if not logo_path.is_file():
        raise FileNotFoundError(f"Logo file not found at: {logo_path}")

    # Clean markdown and style MITRE tags
    lines = markdown_text.splitlines()
    if lines and lines[0].strip().startswith("#"):
        lines = lines[1:]
    clean_md = "\n".join(lines)

    def style_mitre_tags(md_text):
        # Match MITRE codes even in structured lines
        return re.sub(r"(T\d{4}(?:\.\d{3})?)", r'<span class="mitre">\1</span>', md_text)

    styled_md = style_mitre_tags(clean_md)
    html_body = markdown.markdown(styled_md)

    # Cover page HTML
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

    # Full HTML with style
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

    # Output path
    output_file = os.path.join(
        r"C:\Users\zacha\OneDrive\Documents\Reports\ThreatReports",
        f"weekly_threat_report_{datetime.now().strftime('%Y-%m-%d')}.pdf"
    )

    # wkhtmltopdf config
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    # Generate PDF
    pdfkit.from_string(
        full_html,
        output_file,
        configuration=config,
        options={"enable-local-file-access": ""}
    )

    print(f"✅ PDF created: {output_file}")

except Exception as e:
    print("❌ Error while running script:")
    traceback.print_exc()
