def generate_markdown(articles):
    report = "# Weekly Threat Report\n\n"
    for article in articles:
        report += f"## {article['title']}\n"
        report += f"- **Source**: {article['source']}\n"
        report += f"- **Published**: {article['published'].strftime('%Y-%m-%d')}\n"
        report += f"- **Link**: {article['link']}\n"

        # Clean and display BLUF
        bluf_text = article.get('bluf', '[Not available]').removeprefix("BLUF: ").strip()
        report += f"- **BLUF**: {bluf_text}\n"

        # Always display MITRE ATT&CK line
        mitre_text = article.get('mitre', '').strip()

        # Normalize output
        if not mitre_text or mitre_text in {"[None detected]", "None"}:
            mitre_text = "[Empty]"

        report += f"- **MITRE ATT&CK Techniques**: {mitre_text}\n"

    return report
