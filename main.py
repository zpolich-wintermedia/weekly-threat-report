from fetch_feeds import fetch_articles, get_full_article
from summarize import generate_bluf_and_mitre
from report_generator import generate_markdown

def main():
    articles = fetch_articles()

    for article in articles:
        text = get_full_article(article['link'])
        bluf, mitre = generate_bluf_and_mitre(text)

        article['bluf'] = bluf
        article['mitre'] = mitre

    markdown = generate_markdown(articles)

    with open("weekly_threat_report.md", "w", encoding="utf-8") as f:
        f.write(markdown)

if __name__ == "__main__":
    main()
