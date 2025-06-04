{
    "chunks": [
        {
            "type": "txt",
            "chunk_number": 1,
            "lines": [
                {
                    "line_number": 1,
                    "text": "-------config.py---------"
                },
                {
                    "line_number": 2,
                    "text": "OPENAI_API_KEY = \"privatekey\""
                },
                {
                    "line_number": 3,
                    "text": ""
                },
                {
                    "line_number": 4,
                    "text": "FEED_URLS = {"
                },
                {
                    "line_number": 5,
                    "text": "\"BleepingComputer\": \"https://www.bleepingcomputer.com/feed/\","
                },
                {
                    "line_number": 6,
                    "text": "\"The Hacker News\": \"https://feeds.feedburner.com/TheHackersNews\","
                },
                {
                    "line_number": 7,
                    "text": "\"CISA\": \"https://www.cisa.gov/news.xml\""
                },
                {
                    "line_number": 8,
                    "text": "}"
                },
                {
                    "line_number": 9,
                    "text": ""
                },
                {
                    "line_number": 10,
                    "text": "--------export_pdf.py----------"
                },
                {
                    "line_number": 11,
                    "text": "import markdown"
                },
                {
                    "line_number": 12,
                    "text": "import pdfkit"
                },
                {
                    "line_number": 13,
                    "text": "import re"
                },
                {
                    "line_number": 14,
                    "text": "from datetime import datetime"
                },
                {
                    "line_number": 15,
                    "text": "import os"
                },
                {
                    "line_number": 16,
                    "text": "import pathlib"
                },
                {
                    "line_number": 17,
                    "text": ""
                },
                {
                    "line_number": 18,
                    "text": "# === Logo Setup ==="
                },
                {
                    "line_number": 19,
                    "text": "logo_filename = \"logo.png\""
                },
                {
                    "line_number": 20,
                    "text": "logo_path = pathlib.Path(logo_filename).resolve()"
                },
                {
                    "line_number": 21,
                    "text": "logo_uri = logo_path.as_uri()"
                },
                {
                    "line_number": 22,
                    "text": ""
                },
                {
                    "line_number": 23,
                    "text": "if not logo_path.is_file():"
                },
                {
                    "line_number": 24,
                    "text": "raise FileNotFoundError(f\"Logo file not found at: {logo_path}\")"
                },
                {
                    "line_number": 25,
                    "text": ""
                },
                {
                    "line_number": 26,
                    "text": "# === Load and clean markdown ==="
                },
                {
                    "line_number": 27,
                    "text": "with open(\"weekly_threat_report.md\", \"r\", encoding=\"utf-8\") as f:"
                },
                {
                    "line_number": 28,
                    "text": "lines = f.readlines()"
                },
                {
                    "line_number": 29,
                    "text": ""
                },
                {
                    "line_number": 30,
                    "text": "# Remove first-level markdown title if present"
                },
                {
                    "line_number": 31,
                    "text": "if lines and lines[0].strip().startswith(\"#\"):"
                },
                {
                    "line_number": 32,
                    "text": "lines = lines[1:]"
                },
                {
                    "line_number": 33,
                    "text": ""
                },
                {
                    "line_number": 34,
                    "text": "clean_md = \"\".join(lines)"
                },
                {
                    "line_number": 35,
                    "text": ""
                },
                {
                    "line_number": 36,
                    "text": "# === Highlight MITRE Techniques ==="
                },
                {
                    "line_number": 37,
                    "text": "def style_mitre_tags(md_text):"
                },
                {
                    "line_number": 38,
                    "text": "return re.sub(r\"\\b(T\\d{4}(?:\\.\\d{3})?)\\b\", r'<span class=\"mitre\">\\1</span>', md_text)"
                },
                {
                    "line_number": 39,
                    "text": ""
                },
                {
                    "line_number": 40,
                    "text": "styled_md = style_mitre_tags(clean_md)"
                },
                {
                    "line_number": 41,
                    "text": "html_body = markdown.markdown(styled_md)"
                },
                {
                    "line_number": 42,
                    "text": ""
                },
                {
                    "line_number": 43,
                    "text": "# === Cover page content ==="
                },
                {
                    "line_number": 44,
                    "text": "report_date = datetime.now().strftime(\"%B %d, %Y\")"
                },
                {
                    "line_number": 45,
                    "text": "cover_html = f\"\"\""
                },
                {
                    "line_number": 46,
                    "text": "<div class=\"cover\">"
                },
                {
                    "line_number": 47,
                    "text": "<img src=\"{logo_uri}\" alt=\"Company Logo\" style=\"width:200px; display:block; margin: 0 auto 40px auto;\">"
                },
                {
                    "line_number": 48,
                    "text": "<h1>Weekly Threat Report</h1>"
                },
                {
                    "line_number": 49,
                    "text": "<p class=\"meta\">Date: {report_date}</p>"
                },
                {
                    "line_number": 50,
                    "text": "<p class=\"meta\">Prepared by: TechCXO Security Team</p>"
                },
                {
                    "line_number": 51,
                    "text": "</div>"
                },
                {
                    "line_number": 52,
                    "text": "<div class=\"page-break\"></div>"
                },
                {
                    "line_number": 53,
                    "text": "\"\"\""
                },
                {
                    "line_number": 54,
                    "text": ""
                },
                {
                    "line_number": 55,
                    "text": "# === Final HTML document ==="
                },
                {
                    "line_number": 56,
                    "text": "full_html = f\"\"\""
                },
                {
                    "line_number": 57,
                    "text": "<!DOCTYPE html>"
                },
                {
                    "line_number": 58,
                    "text": "<html>"
                },
                {
                    "line_number": 59,
                    "text": "<head>"
                },
                {
                    "line_number": 60,
                    "text": "<meta charset=\"utf-8\">"
                },
                {
                    "line_number": 61,
                    "text": "<title>Weekly Threat Report</title>"
                },
                {
                    "line_number": 62,
                    "text": "<style>"
                },
                {
                    "line_number": 63,
                    "text": "@page {{"
                },
                {
                    "line_number": 64,
                    "text": "size: A4;"
                },
                {
                    "line_number": 65,
                    "text": "margin: 30mm 20mm 20mm 20mm;"
                },
                {
                    "line_number": 66,
                    "text": "@top-left {{"
                },
                {
                    "line_number": 67,
                    "text": "content: url(\"{logo_uri}\");"
                },
                {
                    "line_number": 68,
                    "text": "vertical-align: middle;"
                },
                {
                    "line_number": 69,
                    "text": "margin: 10px;"
                },
                {
                    "line_number": 70,
                    "text": "}}"
                },
                {
                    "line_number": 71,
                    "text": "@bottom-center {{"
                },
                {
                    "line_number": 72,
                    "text": "content: \"Page \" counter(page);"
                },
                {
                    "line_number": 73,
                    "text": "font-size: 10px;"
                },
                {
                    "line_number": 74,
                    "text": "color: #555;"
                },
                {
                    "line_number": 75,
                    "text": "}}"
                },
                {
                    "line_number": 76,
                    "text": "}}"
                },
                {
                    "line_number": 77,
                    "text": "body {{"
                },
                {
                    "line_number": 78,
                    "text": "font-family: \"Segoe UI\", Tahoma, sans-serif;"
                },
                {
                    "line_number": 79,
                    "text": "margin: 40px;"
                },
                {
                    "line_number": 80,
                    "text": "color: #2b2b2b;"
                },
                {
                    "line_number": 81,
                    "text": "line-height: 1.6;"
                },
                {
                    "line_number": 82,
                    "text": "}}"
                },
                {
                    "line_number": 83,
                    "text": "h1 {{"
                },
                {
                    "line_number": 84,
                    "text": "text-align: center;"
                },
                {
                    "line_number": 85,
                    "text": "font-size: 28px;"
                },
                {
                    "line_number": 86,
                    "text": "border-bottom: 2px solid #333;"
                },
                {
                    "line_number": 87,
                    "text": "padding-bottom: 5px;"
                },
                {
                    "line_number": 88,
                    "text": "}}"
                },
                {
                    "line_number": 89,
                    "text": "h2 {{"
                },
                {
                    "line_number": 90,
                    "text": "color: #003366;"
                },
                {
                    "line_number": 91,
                    "text": "margin-top: 30px;"
                },
                {
                    "line_number": 92,
                    "text": "}}"
                },
                {
                    "line_number": 93,
                    "text": "a {{"
                },
                {
                    "line_number": 94,
                    "text": "color: #1a0dab;"
                },
                {
                    "line_number": 95,
                    "text": "text-decoration: none;"
                },
                {
                    "line_number": 96,
                    "text": "}}"
                },
                {
                    "line_number": 97,
                    "text": ".meta {{"
                },
                {
                    "line_number": 98,
                    "text": "font-size: 14px;"
                },
                {
                    "line_number": 99,
                    "text": "color: #555;"
                },
                {
                    "line_number": 100,
                    "text": "text-align: center;"
                },
                {
                    "line_number": 101,
                    "text": "}}"
                },
                {
                    "line_number": 102,
                    "text": ".cover {{"
                },
                {
                    "line_number": 103,
                    "text": "margin-top: 200px;"
                },
                {
                    "line_number": 104,
                    "text": "}}"
                },
                {
                    "line_number": 105,
                    "text": ".page-break {{"
                },
                {
                    "line_number": 106,
                    "text": "page-break-after: always;"
                },
                {
                    "line_number": 107,
                    "text": "}}"
                },
                {
                    "line_number": 108,
                    "text": ".mitre {{"
                },
                {
                    "line_number": 109,
                    "text": "display: inline-block;"
                },
                {
                    "line_number": 110,
                    "text": "background-color: #f0f0f0;"
                },
                {
                    "line_number": 111,
                    "text": "padding: 4px 8px;"
                },
                {
                    "line_number": 112,
                    "text": "margin: 3px 3px 3px 0;"
                },
                {
                    "line_number": 113,
                    "text": "font-size: 12px;"
                },
                {
                    "line_number": 114,
                    "text": "font-weight: bold;"
                },
                {
                    "line_number": 115,
                    "text": "border: 1px solid #ccc;"
                },
                {
                    "line_number": 116,
                    "text": "border-radius: 4px;"
                },
                {
                    "line_number": 117,
                    "text": "color: #333;"
                },
                {
                    "line_number": 118,
                    "text": "}}"
                },
                {
                    "line_number": 119,
                    "text": "</style>"
                },
                {
                    "line_number": 120,
                    "text": "</head>"
                },
                {
                    "line_number": 121,
                    "text": "<body>"
                },
                {
                    "line_number": 122,
                    "text": "{cover_html}"
                },
                {
                    "line_number": 123,
                    "text": "{html_body}"
                },
                {
                    "line_number": 124,
                    "text": "</body>"
                },
                {
                    "line_number": 125,
                    "text": "</html>"
                },
                {
                    "line_number": 126,
                    "text": "\"\"\""
                },
                {
                    "line_number": 127,
                    "text": ""
                },
                {
                    "line_number": 128,
                    "text": "# === Output PDF location ==="
                },
                {
                    "line_number": 129,
                    "text": "output_file = os.path.join("
                },
                {
                    "line_number": 130,
                    "text": "r\"C:\\Users\\zacha\\OneDrive\\Documents\\Reports\\ThreatReports\","
                },
                {
                    "line_number": 131,
                    "text": "f\"weekly_threat_report_{datetime.now().strftime('%Y-%m-%d')}.pdf\""
                },
                {
                    "line_number": 132,
                    "text": ")"
                },
                {
                    "line_number": 133,
                    "text": ""
                },
                {
                    "line_number": 134,
                    "text": "# === wkhtmltopdf Configuration ==="
                },
                {
                    "line_number": 135,
                    "text": "config = pdfkit.configuration(wkhtmltopdf=r\"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe\")"
                },
                {
                    "line_number": 136,
                    "text": ""
                },
                {
                    "line_number": 137,
                    "text": "# === PDF Generation ==="
                },
                {
                    "line_number": 138,
                    "text": "pdfkit.from_string("
                },
                {
                    "line_number": 139,
                    "text": "full_html,"
                },
                {
                    "line_number": 140,
                    "text": "output_file,"
                },
                {
                    "line_number": 141,
                    "text": "configuration=config,"
                },
                {
                    "line_number": 142,
                    "text": "options={\"enable-local-file-access\": \"\"}"
                },
                {
                    "line_number": 143,
                    "text": ")"
                },
                {
                    "line_number": 144,
                    "text": ""
                },
                {
                    "line_number": 145,
                    "text": "print(f\"\u2705 PDF created: {output_file}\")"
                },
                {
                    "line_number": 146,
                    "text": ""
                },
                {
                    "line_number": 147,
                    "text": "-------fetch_feeds.py-------------------"
                },
                {
                    "line_number": 148,
                    "text": "import markdown"
                },
                {
                    "line_number": 149,
                    "text": "import pdfkit"
                },
                {
                    "line_number": 150,
                    "text": "import re"
                },
                {
                    "line_number": 151,
                    "text": "from datetime import datetime"
                },
                {
                    "line_number": 152,
                    "text": "import os"
                },
                {
                    "line_number": 153,
                    "text": "import pathlib"
                },
                {
                    "line_number": 154,
                    "text": ""
                },
                {
                    "line_number": 155,
                    "text": "# === Logo Setup ==="
                },
                {
                    "line_number": 156,
                    "text": "logo_filename = \"logo.png\""
                },
                {
                    "line_number": 157,
                    "text": "logo_path = pathlib.Path(logo_filename).resolve()"
                },
                {
                    "line_number": 158,
                    "text": "logo_uri = logo_path.as_uri()"
                },
                {
                    "line_number": 159,
                    "text": ""
                },
                {
                    "line_number": 160,
                    "text": "if not logo_path.is_file():"
                },
                {
                    "line_number": 161,
                    "text": "raise FileNotFoundError(f\"Logo file not found at: {logo_path}\")"
                },
                {
                    "line_number": 162,
                    "text": ""
                },
                {
                    "line_number": 163,
                    "text": "# === Load and clean markdown ==="
                },
                {
                    "line_number": 164,
                    "text": "with open(\"weekly_threat_report.md\", \"r\", encoding=\"utf-8\") as f:"
                },
                {
                    "line_number": 165,
                    "text": "lines = f.readlines()"
                },
                {
                    "line_number": 166,
                    "text": ""
                },
                {
                    "line_number": 167,
                    "text": "# Remove first-level markdown title if present"
                },
                {
                    "line_number": 168,
                    "text": "if lines and lines[0].strip().startswith(\"#\"):"
                },
                {
                    "line_number": 169,
                    "text": "lines = lines[1:]"
                },
                {
                    "line_number": 170,
                    "text": ""
                },
                {
                    "line_number": 171,
                    "text": "clean_md = \"\".join(lines)"
                },
                {
                    "line_number": 172,
                    "text": ""
                },
                {
                    "line_number": 173,
                    "text": "# === Highlight MITRE Techniques ==="
                },
                {
                    "line_number": 174,
                    "text": "def style_mitre_tags(md_text):"
                },
                {
                    "line_number": 175,
                    "text": "return re.sub(r\"\\b(T\\d{4}(?:\\.\\d{3})?)\\b\", r'<span class=\"mitre\">\\1</span>', md_text)"
                },
                {
                    "line_number": 176,
                    "text": ""
                },
                {
                    "line_number": 177,
                    "text": "styled_md = style_mitre_tags(clean_md)"
                },
                {
                    "line_number": 178,
                    "text": "html_body = markdown.markdown(styled_md)"
                },
                {
                    "line_number": 179,
                    "text": ""
                },
                {
                    "line_number": 180,
                    "text": "# === Cover page content ==="
                },
                {
                    "line_number": 181,
                    "text": "report_date = datetime.now().strftime(\"%B %d, %Y\")"
                },
                {
                    "line_number": 182,
                    "text": "cover_html = f\"\"\""
                },
                {
                    "line_number": 183,
                    "text": "<div class=\"cover\">"
                },
                {
                    "line_number": 184,
                    "text": "<img src=\"{logo_uri}\" alt=\"Company Logo\" style=\"width:200px; display:block; margin: 0 auto 40px auto;\">"
                },
                {
                    "line_number": 185,
                    "text": "<h1>Weekly Threat Report</h1>"
                },
                {
                    "line_number": 186,
                    "text": "<p class=\"meta\">Date: {report_date}</p>"
                },
                {
                    "line_number": 187,
                    "text": "<p class=\"meta\">Prepared by: TechCXO Security Team</p>"
                },
                {
                    "line_number": 188,
                    "text": "</div>"
                },
                {
                    "line_number": 189,
                    "text": "<div class=\"page-break\"></div>"
                },
                {
                    "line_number": 190,
                    "text": "\"\"\""
                },
                {
                    "line_number": 191,
                    "text": ""
                },
                {
                    "line_number": 192,
                    "text": "# === Final HTML document ==="
                },
                {
                    "line_number": 193,
                    "text": "full_html = f\"\"\""
                },
                {
                    "line_number": 194,
                    "text": "<!DOCTYPE html>"
                },
                {
                    "line_number": 195,
                    "text": "<html>"
                },
                {
                    "line_number": 196,
                    "text": "<head>"
                },
                {
                    "line_number": 197,
                    "text": "<meta charset=\"utf-8\">"
                },
                {
                    "line_number": 198,
                    "text": "<title>Weekly Threat Report</title>"
                },
                {
                    "line_number": 199,
                    "text": "<style>"
                },
                {
                    "line_number": 200,
                    "text": "@page {{"
                },
                {
                    "line_number": 201,
                    "text": "size: A4;"
                },
                {
                    "line_number": 202,
                    "text": "margin: 30mm 20mm 20mm 20mm;"
                },
                {
                    "line_number": 203,
                    "text": "@top-left {{"
                },
                {
                    "line_number": 204,
                    "text": "content: url(\"{logo_uri}\");"
                },
                {
                    "line_number": 205,
                    "text": "vertical-align: middle;"
                },
                {
                    "line_number": 206,
                    "text": "margin: 10px;"
                },
                {
                    "line_number": 207,
                    "text": "}}"
                },
                {
                    "line_number": 208,
                    "text": "@bottom-center {{"
                },
                {
                    "line_number": 209,
                    "text": "content: \"Page \" counter(page);"
                },
                {
                    "line_number": 210,
                    "text": "font-size: 10px;"
                },
                {
                    "line_number": 211,
                    "text": "color: #555;"
                },
                {
                    "line_number": 212,
                    "text": "}}"
                },
                {
                    "line_number": 213,
                    "text": "}}"
                },
                {
                    "line_number": 214,
                    "text": "body {{"
                },
                {
                    "line_number": 215,
                    "text": "font-family: \"Segoe UI\", Tahoma, sans-serif;"
                },
                {
                    "line_number": 216,
                    "text": "margin: 40px;"
                },
                {
                    "line_number": 217,
                    "text": "color: #2b2b2b;"
                },
                {
                    "line_number": 218,
                    "text": "line-height: 1.6;"
                },
                {
                    "line_number": 219,
                    "text": "}}"
                },
                {
                    "line_number": 220,
                    "text": "h1 {{"
                },
                {
                    "line_number": 221,
                    "text": "text-align: center;"
                },
                {
                    "line_number": 222,
                    "text": "font-size: 28px;"
                },
                {
                    "line_number": 223,
                    "text": "border-bottom: 2px solid #333;"
                },
                {
                    "line_number": 224,
                    "text": "padding-bottom: 5px;"
                },
                {
                    "line_number": 225,
                    "text": "}}"
                },
                {
                    "line_number": 226,
                    "text": "h2 {{"
                },
                {
                    "line_number": 227,
                    "text": "color: #003366;"
                },
                {
                    "line_number": 228,
                    "text": "margin-top: 30px;"
                },
                {
                    "line_number": 229,
                    "text": "}}"
                },
                {
                    "line_number": 230,
                    "text": "a {{"
                },
                {
                    "line_number": 231,
                    "text": "color: #1a0dab;"
                },
                {
                    "line_number": 232,
                    "text": "text-decoration: none;"
                },
                {
                    "line_number": 233,
                    "text": "}}"
                },
                {
                    "line_number": 234,
                    "text": ".meta {{"
                },
                {
                    "line_number": 235,
                    "text": "font-size: 14px;"
                },
                {
                    "line_number": 236,
                    "text": "color: #555;"
                },
                {
                    "line_number": 237,
                    "text": "text-align: center;"
                },
                {
                    "line_number": 238,
                    "text": "}}"
                },
                {
                    "line_number": 239,
                    "text": ".cover {{"
                },
                {
                    "line_number": 240,
                    "text": "margin-top: 200px;"
                },
                {
                    "line_number": 241,
                    "text": "}}"
                },
                {
                    "line_number": 242,
                    "text": ".page-break {{"
                },
                {
                    "line_number": 243,
                    "text": "page-break-after: always;"
                },
                {
                    "line_number": 244,
                    "text": "}}"
                },
                {
                    "line_number": 245,
                    "text": ".mitre {{"
                },
                {
                    "line_number": 246,
                    "text": "display: inline-block;"
                },
                {
                    "line_number": 247,
                    "text": "background-color: #f0f0f0;"
                },
                {
                    "line_number": 248,
                    "text": "padding: 4px 8px;"
                },
                {
                    "line_number": 249,
                    "text": "margin: 3px 3px 3px 0;"
                },
                {
                    "line_number": 250,
                    "text": "font-size: 12px;"
                },
                {
                    "line_number": 251,
                    "text": "font-weight: bold;"
                },
                {
                    "line_number": 252,
                    "text": "border: 1px solid #ccc;"
                },
                {
                    "line_number": 253,
                    "text": "border-radius: 4px;"
                },
                {
                    "line_number": 254,
                    "text": "color: #333;"
                },
                {
                    "line_number": 255,
                    "text": "}}"
                },
                {
                    "line_number": 256,
                    "text": "</style>"
                },
                {
                    "line_number": 257,
                    "text": "</head>"
                },
                {
                    "line_number": 258,
                    "text": "<body>"
                },
                {
                    "line_number": 259,
                    "text": "{cover_html}"
                },
                {
                    "line_number": 260,
                    "text": "{html_body}"
                },
                {
                    "line_number": 261,
                    "text": "</body>"
                },
                {
                    "line_number": 262,
                    "text": "</html>"
                },
                {
                    "line_number": 263,
                    "text": "\"\"\""
                },
                {
                    "line_number": 264,
                    "text": ""
                },
                {
                    "line_number": 265,
                    "text": "# === Output PDF location ==="
                },
                {
                    "line_number": 266,
                    "text": "output_file = os.path.join("
                },
                {
                    "line_number": 267,
                    "text": "r\"C:\\Users\\zacha\\OneDrive\\Documents\\Reports\\ThreatReports\","
                },
                {
                    "line_number": 268,
                    "text": "f\"weekly_threat_report_{datetime.now().strftime('%Y-%m-%d')}.pdf\""
                },
                {
                    "line_number": 269,
                    "text": ")"
                },
                {
                    "line_number": 270,
                    "text": ""
                },
                {
                    "line_number": 271,
                    "text": "# === wkhtmltopdf Configuration ==="
                },
                {
                    "line_number": 272,
                    "text": "config = pdfkit.configuration(wkhtmltopdf=r\"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe\")"
                },
                {
                    "line_number": 273,
                    "text": ""
                },
                {
                    "line_number": 274,
                    "text": "# === PDF Generation ==="
                },
                {
                    "line_number": 275,
                    "text": "pdfkit.from_string("
                },
                {
                    "line_number": 276,
                    "text": "full_html,"
                },
                {
                    "line_number": 277,
                    "text": "output_file,"
                },
                {
                    "line_number": 278,
                    "text": "configuration=config,"
                },
                {
                    "line_number": 279,
                    "text": "options={\"enable-local-file-access\": \"\"}"
                },
                {
                    "line_number": 280,
                    "text": ")"
                },
                {
                    "line_number": 281,
                    "text": ""
                },
                {
                    "line_number": 282,
                    "text": "print(f\"\u2705 PDF created: {output_file}\")"
                },
                {
                    "line_number": 283,
                    "text": ""
                },
                {
                    "line_number": 284,
                    "text": "----------main.py-----------------"
                },
                {
                    "line_number": 285,
                    "text": "from fetch_feeds import fetch_articles, get_full_article"
                },
                {
                    "line_number": 286,
                    "text": "from summarize import generate_bluf_and_mitre"
                },
                {
                    "line_number": 287,
                    "text": "from report_generator import generate_markdown"
                },
                {
                    "line_number": 288,
                    "text": ""
                },
                {
                    "line_number": 289,
                    "text": "def main():"
                },
                {
                    "line_number": 290,
                    "text": "articles = fetch_articles()"
                },
                {
                    "line_number": 291,
                    "text": ""
                },
                {
                    "line_number": 292,
                    "text": "for article in articles:"
                },
                {
                    "line_number": 293,
                    "text": "text = get_full_article(article['link'])"
                },
                {
                    "line_number": 294,
                    "text": "bluf, mitre = generate_bluf_and_mitre(text)"
                },
                {
                    "line_number": 295,
                    "text": ""
                },
                {
                    "line_number": 296,
                    "text": "article['bluf'] = bluf"
                },
                {
                    "line_number": 297,
                    "text": "article['mitre'] = mitre"
                },
                {
                    "line_number": 298,
                    "text": ""
                },
                {
                    "line_number": 299,
                    "text": "markdown = generate_markdown(articles)"
                },
                {
                    "line_number": 300,
                    "text": ""
                },
                {
                    "line_number": 301,
                    "text": "with open(\"weekly_threat_report.md\", \"w\", encoding=\"utf-8\") as f:"
                },
                {
                    "line_number": 302,
                    "text": "f.write(markdown)"
                },
                {
                    "line_number": 303,
                    "text": ""
                },
                {
                    "line_number": 304,
                    "text": "if __name__ == \"__main__\":"
                },
                {
                    "line_number": 305,
                    "text": "main()"
                },
                {
                    "line_number": 306,
                    "text": ""
                },
                {
                    "line_number": 307,
                    "text": "------report_generator.py-----------------"
                },
                {
                    "line_number": 308,
                    "text": "def generate_markdown(articles):"
                },
                {
                    "line_number": 309,
                    "text": "report = \"# Weekly Threat Report\\n\\n\""
                },
                {
                    "line_number": 310,
                    "text": "for article in articles:"
                },
                {
                    "line_number": 311,
                    "text": "report += f\"## {article['title']}\\n\""
                },
                {
                    "line_number": 312,
                    "text": "report += f\"- **Source**: {article['source']}\\n\""
                },
                {
                    "line_number": 313,
                    "text": "report += f\"- **Published**: {article['published'].strftime('%Y-%m-%d')}\\n\""
                },
                {
                    "line_number": 314,
                    "text": "report += f\"- **Link**: {article['link']}\\n\""
                },
                {
                    "line_number": 315,
                    "text": ""
                },
                {
                    "line_number": 316,
                    "text": "# Clean and display BLUF"
                },
                {
                    "line_number": 317,
                    "text": "bluf_text = article.get('bluf', '[Not available]').removeprefix(\"BLUF: \").strip()"
                },
                {
                    "line_number": 318,
                    "text": "report += f\"- **BLUF**: {bluf_text}\\n\""
                },
                {
                    "line_number": 319,
                    "text": ""
                },
                {
                    "line_number": 320,
                    "text": "# Always display MITRE ATT&CK line"
                },
                {
                    "line_number": 321,
                    "text": "mitre_text = article.get('mitre', '').strip()"
                },
                {
                    "line_number": 322,
                    "text": ""
                },
                {
                    "line_number": 323,
                    "text": "# Normalize output"
                },
                {
                    "line_number": 324,
                    "text": "if not mitre_text or mitre_text in {\"[None detected]\", \"None\"}:"
                },
                {
                    "line_number": 325,
                    "text": "mitre_text = \"[Empty]\""
                },
                {
                    "line_number": 326,
                    "text": ""
                },
                {
                    "line_number": 327,
                    "text": "report += f\"- **MITRE ATT&CK Techniques**: {mitre_text}\\n\""
                },
                {
                    "line_number": 328,
                    "text": ""
                },
                {
                    "line_number": 329,
                    "text": ""
                },
                {
                    "line_number": 330,
                    "text": "return report"
                },
                {
                    "line_number": 331,
                    "text": ""
                },
                {
                    "line_number": 332,
                    "text": "-------run_weekly_report.py---------"
                },
                {
                    "line_number": 333,
                    "text": "import os"
                },
                {
                    "line_number": 334,
                    "text": "import traceback"
                },
                {
                    "line_number": 335,
                    "text": "from fetch_feeds import fetch_articles, get_full_article"
                },
                {
                    "line_number": 336,
                    "text": "from summarize import generate_bluf_and_mitre"
                },
                {
                    "line_number": 337,
                    "text": "from report_generator import generate_markdown"
                },
                {
                    "line_number": 338,
                    "text": "import markdown"
                },
                {
                    "line_number": 339,
                    "text": "import pdfkit"
                },
                {
                    "line_number": 340,
                    "text": "import re"
                },
                {
                    "line_number": 341,
                    "text": "from datetime import datetime"
                },
                {
                    "line_number": 342,
                    "text": "import pathlib"
                },
                {
                    "line_number": 343,
                    "text": ""
                },
                {
                    "line_number": 344,
                    "text": "print(\"\ud83d\udccc Running Weekly Threat Report script...\")"
                },
                {
                    "line_number": 345,
                    "text": ""
                },
                {
                    "line_number": 346,
                    "text": "try:"
                },
                {
                    "line_number": 347,
                    "text": "# === STEP 1: Fetch + Summarize Articles ==="
                },
                {
                    "line_number": 348,
                    "text": "articles = fetch_articles()"
                },
                {
                    "line_number": 349,
                    "text": "for article in articles:"
                },
                {
                    "line_number": 350,
                    "text": "full_text = get_full_article(article['link'])"
                },
                {
                    "line_number": 351,
                    "text": "bluf, mitre_tags = generate_bluf_and_mitre(full_text)"
                },
                {
                    "line_number": 352,
                    "text": "article['bluf'] = bluf"
                },
                {
                    "line_number": 353,
                    "text": "article['mitre'] = mitre_tags"
                },
                {
                    "line_number": 354,
                    "text": ""
                },
                {
                    "line_number": 355,
                    "text": "# === STEP 2: Generate Markdown ==="
                },
                {
                    "line_number": 356,
                    "text": "markdown_text = generate_markdown(articles)"
                },
                {
                    "line_number": 357,
                    "text": "with open(\"weekly_threat_report.md\", \"w\", encoding=\"utf-8\") as f:"
                },
                {
                    "line_number": 358,
                    "text": "f.write(markdown_text)"
                },
                {
                    "line_number": 359,
                    "text": "print(\"\u2705 Markdown report generated.\")"
                },
                {
                    "line_number": 360,
                    "text": ""
                },
                {
                    "line_number": 361,
                    "text": "# === STEP 3: Convert Markdown to PDF ==="
                },
                {
                    "line_number": 362,
                    "text": ""
                },
                {
                    "line_number": 363,
                    "text": "# Logo handling"
                },
                {
                    "line_number": 364,
                    "text": "logo_filename = \"logo.png\""
                },
                {
                    "line_number": 365,
                    "text": "logo_path = pathlib.Path(logo_filename).resolve()"
                },
                {
                    "line_number": 366,
                    "text": "logo_uri = logo_path.as_uri()"
                },
                {
                    "line_number": 367,
                    "text": ""
                },
                {
                    "line_number": 368,
                    "text": "if not logo_path.is_file():"
                },
                {
                    "line_number": 369,
                    "text": "raise FileNotFoundError(f\"Logo file not found at: {logo_path}\")"
                },
                {
                    "line_number": 370,
                    "text": ""
                },
                {
                    "line_number": 371,
                    "text": "# Clean markdown and style MITRE tags"
                },
                {
                    "line_number": 372,
                    "text": "lines = markdown_text.splitlines()"
                },
                {
                    "line_number": 373,
                    "text": "if lines and lines[0].strip().startswith(\"#\"):"
                },
                {
                    "line_number": 374,
                    "text": "lines = lines[1:]"
                },
                {
                    "line_number": 375,
                    "text": "clean_md = \"\\n\".join(lines)"
                },
                {
                    "line_number": 376,
                    "text": ""
                },
                {
                    "line_number": 377,
                    "text": "def style_mitre_tags(md_text):"
                },
                {
                    "line_number": 378,
                    "text": "# Match MITRE codes even in structured lines"
                },
                {
                    "line_number": 379,
                    "text": "return re.sub(r\"(T\\d{4}(?:\\.\\d{3})?)\", r'<span class=\"mitre\">\\1</span>', md_text)"
                },
                {
                    "line_number": 380,
                    "text": ""
                },
                {
                    "line_number": 381,
                    "text": ""
                },
                {
                    "line_number": 382,
                    "text": "styled_md = style_mitre_tags(clean_md)"
                },
                {
                    "line_number": 383,
                    "text": "html_body = markdown.markdown(styled_md)"
                },
                {
                    "line_number": 384,
                    "text": ""
                },
                {
                    "line_number": 385,
                    "text": "# Cover page HTML"
                },
                {
                    "line_number": 386,
                    "text": "report_date = datetime.now().strftime(\"%B %d, %Y\")"
                },
                {
                    "line_number": 387,
                    "text": "cover_html = f\"\"\""
                },
                {
                    "line_number": 388,
                    "text": "<div class=\"cover\">"
                },
                {
                    "line_number": 389,
                    "text": "<img src=\"{logo_uri}\" alt=\"Company Logo\" style=\"width:200px; display:block; margin: 0 auto 40px auto;\">"
                },
                {
                    "line_number": 390,
                    "text": "<h1>Weekly Threat Report</h1>"
                },
                {
                    "line_number": 391,
                    "text": "<p class=\"meta\">Date: {report_date}</p>"
                },
                {
                    "line_number": 392,
                    "text": "<p class=\"meta\">Prepared by: TechCXO Security Team</p>"
                },
                {
                    "line_number": 393,
                    "text": "</div>"
                },
                {
                    "line_number": 394,
                    "text": "<div class=\"page-break\"></div>"
                },
                {
                    "line_number": 395,
                    "text": "\"\"\""
                },
                {
                    "line_number": 396,
                    "text": ""
                },
                {
                    "line_number": 397,
                    "text": "# Full HTML with style"
                },
                {
                    "line_number": 398,
                    "text": "full_html = f\"\"\""
                },
                {
                    "line_number": 399,
                    "text": "<!DOCTYPE html>"
                },
                {
                    "line_number": 400,
                    "text": "<html>"
                },
                {
                    "line_number": 401,
                    "text": "<head>"
                },
                {
                    "line_number": 402,
                    "text": "<meta charset=\"utf-8\">"
                },
                {
                    "line_number": 403,
                    "text": "<title>Weekly Threat Report</title>"
                },
                {
                    "line_number": 404,
                    "text": "<style>"
                },
                {
                    "line_number": 405,
                    "text": "@page {{"
                },
                {
                    "line_number": 406,
                    "text": "size: A4;"
                },
                {
                    "line_number": 407,
                    "text": "margin: 30mm 20mm 20mm 20mm;"
                },
                {
                    "line_number": 408,
                    "text": "@top-left {{"
                },
                {
                    "line_number": 409,
                    "text": "content: url(\"{logo_uri}\");"
                },
                {
                    "line_number": 410,
                    "text": "vertical-align: middle;"
                },
                {
                    "line_number": 411,
                    "text": "margin: 10px;"
                },
                {
                    "line_number": 412,
                    "text": "}}"
                },
                {
                    "line_number": 413,
                    "text": "@bottom-center {{"
                },
                {
                    "line_number": 414,
                    "text": "content: \"Page \" counter(page);"
                },
                {
                    "line_number": 415,
                    "text": "font-size: 10px;"
                },
                {
                    "line_number": 416,
                    "text": "color: #555;"
                },
                {
                    "line_number": 417,
                    "text": "}}"
                },
                {
                    "line_number": 418,
                    "text": "}}"
                },
                {
                    "line_number": 419,
                    "text": "body {{"
                },
                {
                    "line_number": 420,
                    "text": "font-family: \"Segoe UI\", Tahoma, sans-serif;"
                },
                {
                    "line_number": 421,
                    "text": "margin: 40px;"
                },
                {
                    "line_number": 422,
                    "text": "color: #2b2b2b;"
                },
                {
                    "line_number": 423,
                    "text": "line-height: 1.6;"
                },
                {
                    "line_number": 424,
                    "text": "}}"
                },
                {
                    "line_number": 425,
                    "text": "h1 {{"
                },
                {
                    "line_number": 426,
                    "text": "text-align: center;"
                },
                {
                    "line_number": 427,
                    "text": "font-size: 28px;"
                },
                {
                    "line_number": 428,
                    "text": "border-bottom: 2px solid #333;"
                },
                {
                    "line_number": 429,
                    "text": "padding-bottom: 5px;"
                },
                {
                    "line_number": 430,
                    "text": "}}"
                },
                {
                    "line_number": 431,
                    "text": "h2 {{"
                },
                {
                    "line_number": 432,
                    "text": "color: #003366;"
                },
                {
                    "line_number": 433,
                    "text": "margin-top: 30px;"
                },
                {
                    "line_number": 434,
                    "text": "}}"
                },
                {
                    "line_number": 435,
                    "text": "a {{"
                },
                {
                    "line_number": 436,
                    "text": "color: #1a0dab;"
                },
                {
                    "line_number": 437,
                    "text": "text-decoration: none;"
                },
                {
                    "line_number": 438,
                    "text": "}}"
                },
                {
                    "line_number": 439,
                    "text": ".meta {{"
                },
                {
                    "line_number": 440,
                    "text": "font-size: 14px;"
                },
                {
                    "line_number": 441,
                    "text": "color: #555;"
                },
                {
                    "line_number": 442,
                    "text": "text-align: center;"
                },
                {
                    "line_number": 443,
                    "text": "}}"
                },
                {
                    "line_number": 444,
                    "text": ".cover {{"
                },
                {
                    "line_number": 445,
                    "text": "margin-top: 200px;"
                },
                {
                    "line_number": 446,
                    "text": "}}"
                },
                {
                    "line_number": 447,
                    "text": ".page-break {{"
                },
                {
                    "line_number": 448,
                    "text": "page-break-after: always;"
                },
                {
                    "line_number": 449,
                    "text": "}}"
                },
                {
                    "line_number": 450,
                    "text": ".mitre {{"
                },
                {
                    "line_number": 451,
                    "text": "display: inline-block;"
                },
                {
                    "line_number": 452,
                    "text": "background-color: #f0f0f0;"
                },
                {
                    "line_number": 453,
                    "text": "padding: 4px 8px;"
                },
                {
                    "line_number": 454,
                    "text": "margin: 3px 3px 3px 0;"
                },
                {
                    "line_number": 455,
                    "text": "font-size: 12px;"
                },
                {
                    "line_number": 456,
                    "text": "font-weight: bold;"
                },
                {
                    "line_number": 457,
                    "text": "border: 1px solid #ccc;"
                },
                {
                    "line_number": 458,
                    "text": "border-radius: 4px;"
                },
                {
                    "line_number": 459,
                    "text": "color: #333;"
                },
                {
                    "line_number": 460,
                    "text": "}}"
                },
                {
                    "line_number": 461,
                    "text": "</style>"
                },
                {
                    "line_number": 462,
                    "text": "</head>"
                },
                {
                    "line_number": 463,
                    "text": "<body>"
                },
                {
                    "line_number": 464,
                    "text": "{cover_html}"
                },
                {
                    "line_number": 465,
                    "text": "{html_body}"
                },
                {
                    "line_number": 466,
                    "text": "</body>"
                },
                {
                    "line_number": 467,
                    "text": "</html>"
                },
                {
                    "line_number": 468,
                    "text": "\"\"\""
                },
                {
                    "line_number": 469,
                    "text": ""
                },
                {
                    "line_number": 470,
                    "text": "# Output path"
                },
                {
                    "line_number": 471,
                    "text": "output_file = os.path.join("
                },
                {
                    "line_number": 472,
                    "text": "r\"C:\\Users\\zacha\\OneDrive\\Documents\\Reports\\ThreatReports\","
                },
                {
                    "line_number": 473,
                    "text": "f\"weekly_threat_report_{datetime.now().strftime('%Y-%m-%d')}.pdf\""
                },
                {
                    "line_number": 474,
                    "text": ")"
                },
                {
                    "line_number": 475,
                    "text": ""
                },
                {
                    "line_number": 476,
                    "text": "# wkhtmltopdf config"
                },
                {
                    "line_number": 477,
                    "text": "config = pdfkit.configuration(wkhtmltopdf=r\"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe\")"
                },
                {
                    "line_number": 478,
                    "text": ""
                },
                {
                    "line_number": 479,
                    "text": "# Generate PDF"
                },
                {
                    "line_number": 480,
                    "text": "pdfkit.from_string("
                },
                {
                    "line_number": 481,
                    "text": "full_html,"
                },
                {
                    "line_number": 482,
                    "text": "output_file,"
                },
                {
                    "line_number": 483,
                    "text": "configuration=config,"
                },
                {
                    "line_number": 484,
                    "text": "options={\"enable-local-file-access\": \"\"}"
                },
                {
                    "line_number": 485,
                    "text": ")"
                },
                {
                    "line_number": 486,
                    "text": ""
                },
                {
                    "line_number": 487,
                    "text": "print(f\"\u2705 PDF created: {output_file}\")"
                },
                {
                    "line_number": 488,
                    "text": ""
                },
                {
                    "line_number": 489,
                    "text": "except Exception as e:"
                },
                {
                    "line_number": 490,
                    "text": "print(\"\u274c Error while running script:\")"
                },
                {
                    "line_number": 491,
                    "text": "traceback.print_exc()"
                },
                {
                    "line_number": 492,
                    "text": ""
                },
                {
                    "line_number": 493,
                    "text": "---------summarize.py---------"
                },
                {
                    "line_number": 494,
                    "text": "import openai"
                },
                {
                    "line_number": 495,
                    "text": "import re"
                },
                {
                    "line_number": 496,
                    "text": "from config import OPENAI_API_KEY"
                },
                {
                    "line_number": 497,
                    "text": ""
                },
                {
                    "line_number": 498,
                    "text": "client = openai.OpenAI(api_key=OPENAI_API_KEY)"
                },
                {
                    "line_number": 499,
                    "text": ""
                },
                {
                    "line_number": 500,
                    "text": "def generate_bluf_and_mitre(article_text):"
                },
                {
                    "line_number": 501,
                    "text": "if not article_text.strip():"
                },
                {
                    "line_number": 502,
                    "text": "return \"[BLUF skipped: Empty article text]\", \"[MITRE skipped: Empty article text]\""
                },
                {
                    "line_number": 503,
                    "text": ""
                },
                {
                    "line_number": 504,
                    "text": "# === BLUF Prompt ==="
                },
                {
                    "line_number": 505,
                    "text": "bluf_prompt = f\"\"\""
                },
                {
                    "line_number": 506,
                    "text": "You are a cybersecurity threat intelligence analyst. Write a 2-sentence Bottom-Line-Up-Front (BLUF) summary for the following article, focusing on its impact on the U.S. public sector. Include threat actor, technique, and impact if possible."
                },
                {
                    "line_number": 507,
                    "text": ""
                },
                {
                    "line_number": 508,
                    "text": "Article:"
                },
                {
                    "line_number": 509,
                    "text": "{article_text[:3000]}"
                },
                {
                    "line_number": 510,
                    "text": "\"\"\""
                },
                {
                    "line_number": 511,
                    "text": ""
                },
                {
                    "line_number": 512,
                    "text": "# === MITRE Prompt ==="
                },
                {
                    "line_number": 513,
                    "text": "mitre_prompt = f\"\"\""
                },
                {
                    "line_number": 514,
                    "text": "You are a threat intelligence analyst. Identify any relevant MITRE ATT&CK techniques from this article."
                },
                {
                    "line_number": 515,
                    "text": "Respond only with a comma-separated list of MITRE technique IDs (e.g., T1059, T1566). No parentheses, no names."
                },
                {
                    "line_number": 516,
                    "text": "Do not include any other explanation. Limit to 3 techniques max."
                },
                {
                    "line_number": 517,
                    "text": ""
                },
                {
                    "line_number": 518,
                    "text": "Article:"
                },
                {
                    "line_number": 519,
                    "text": "{article_text[:3000]}"
                },
                {
                    "line_number": 520,
                    "text": "\"\"\""
                },
                {
                    "line_number": 521,
                    "text": ""
                },
                {
                    "line_number": 522,
                    "text": "try:"
                },
                {
                    "line_number": 523,
                    "text": "bluf_response = client.chat.completions.create("
                },
                {
                    "line_number": 524,
                    "text": "model=\"gpt-4.1-mini\","
                },
                {
                    "line_number": 525,
                    "text": "messages=[{\"role\": \"user\", \"content\": bluf_prompt}],"
                },
                {
                    "line_number": 526,
                    "text": "temperature=0.5"
                },
                {
                    "line_number": 527,
                    "text": ")"
                },
                {
                    "line_number": 528,
                    "text": "bluf = bluf_response.choices[0].message.content.strip()"
                },
                {
                    "line_number": 529,
                    "text": ""
                },
                {
                    "line_number": 530,
                    "text": "mitre_response = client.chat.completions.create("
                },
                {
                    "line_number": 531,
                    "text": "model=\"gpt-4.1-mini\","
                },
                {
                    "line_number": 532,
                    "text": "messages=[{\"role\": \"user\", \"content\": mitre_prompt}],"
                },
                {
                    "line_number": 533,
                    "text": "temperature=0.3"
                },
                {
                    "line_number": 534,
                    "text": ")"
                },
                {
                    "line_number": 535,
                    "text": "raw_mitre = mitre_response.choices[0].message.content.strip()"
                },
                {
                    "line_number": 536,
                    "text": ""
                },
                {
                    "line_number": 537,
                    "text": "# Extract valid MITRE tags"
                },
                {
                    "line_number": 538,
                    "text": "matches = re.findall(r\"T\\d{4}(?:\\.\\d{3})?\", raw_mitre)"
                },
                {
                    "line_number": 539,
                    "text": "if matches:"
                },
                {
                    "line_number": 540,
                    "text": "mitre = \", \".join(matches)"
                },
                {
                    "line_number": 541,
                    "text": "else:"
                },
                {
                    "line_number": 542,
                    "text": "mitre = \"\"  # Will be handled by report_generator as [Empty]"
                },
                {
                    "line_number": 543,
                    "text": ""
                },
                {
                    "line_number": 544,
                    "text": "return bluf, mitre"
                },
                {
                    "line_number": 545,
                    "text": ""
                },
                {
                    "line_number": 546,
                    "text": "except Exception as e:"
                },
                {
                    "line_number": 547,
                    "text": "return f\"[BLUF failed: {e}]\", f\"[MITRE failed: {e}]\""
                }
            ],
            "token_count": 3014
        }
    ]
}