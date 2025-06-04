import openai
import re
from config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_bluf_and_mitre(article_text):
    if not article_text.strip():
        return "[BLUF skipped: Empty article text]", "[MITRE skipped: Empty article text]"

    # === BLUF Prompt ===
    bluf_prompt = f"""
    You are a cybersecurity threat intelligence analyst. Write a 2-sentence Bottom-Line-Up-Front (BLUF) summary for the following article, focusing on its impact on the U.S. public sector. Include threat actor, technique, and impact if possible.

    Article:
    {article_text[:3000]}
    """

    # === MITRE Prompt ===
    mitre_prompt = f"""
    You are a threat intelligence analyst. Identify any relevant MITRE ATT&CK techniques from this article.
    Respond only with a comma-separated list of MITRE technique IDs (e.g., T1059, T1566). No parentheses, no names.
    Do not include any other explanation. Limit to 3 techniques max.

    Article:
    {article_text[:3000]}
    """

    try:
        bluf_response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": bluf_prompt}],
            temperature=0.5
        )
        bluf = bluf_response.choices[0].message.content.strip()

        mitre_response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": mitre_prompt}],
            temperature=0.3
        )
        raw_mitre = mitre_response.choices[0].message.content.strip()

        # Extract valid MITRE tags
        matches = re.findall(r"T\d{4}(?:\.\d{3})?", raw_mitre)
        if matches:
            mitre = ", ".join(matches)
        else:
            mitre = ""  # Will be handled by report_generator as [Empty]

        return bluf, mitre

    except Exception as e:
        return f"[BLUF failed: {e}]", f"[MITRE failed: {e}]"
