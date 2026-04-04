"""
Newsletter pipeline orchestrator.
Chains: research (or pre-supplied JSON) → infographic → format → output.

Usage:
    # With agent-provided research (primary flow):
    python tools/run_newsletter.py --research-file .tmp/newsletter_data.json "email1@example.com,email2@example.com"

    # With auto-research via OpenRouter (fallback):
    python tools/run_newsletter.py "Topic" "email1@example.com,email2@example.com"

The HTML output is saved to .tmp/newsletter.html and recipient list to .tmp/recipients.txt.
Gmail sending is handled by the agent via Gmail MCP.
"""

import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tools.generate_infographic import generate_infographic
from tools.format_newsletter import format_newsletter

TMP_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".tmp")


def run_pipeline(research: dict, recipients: str) -> dict:
    """Run the newsletter pipeline from research data onward."""
    os.makedirs(TMP_DIR, exist_ok=True)

    topic = research.get("title", "Newsletter")

    # Save research data
    research_path = os.path.join(TMP_DIR, "newsletter_data.json")
    with open(research_path, "w", encoding="utf-8") as f:
        json.dump(research, f, indent=2)

    # Step 1: Generate infographic
    print(f"\n{'='*50}")
    print("STEP 1: Generating infographic...")
    print(f"{'='*50}")
    infographic_prompt = (
        f"Create a clean, modern infographic about: {topic}. "
        f"Include visual representations of these key points: "
        f"{'; '.join(research.get('key_points', [topic])[:3])}. "
        f"Use a professional color palette with blues and purples. "
        f"Make it suitable for a newsletter email."
    )

    infographic_base64 = None
    infographic_url = None
    try:
        infographic = generate_infographic(infographic_prompt)
        infographic_base64 = infographic["image_base64"]
        infographic_url = infographic.get("image_url")
        print(f"Infographic saved to: {infographic['image_path']}")
    except Exception as e:
        print(f"Infographic generation failed (continuing without it): {e}")

    # Step 2: Format HTML
    print(f"\n{'='*50}")
    print("STEP 2: Formatting HTML newsletter...")
    print(f"{'='*50}")

    summary = research.get("summary", "")
    if isinstance(summary, list):
        summary = "<br><br>".join(summary)

    html = format_newsletter(
        title=topic,
        summary=summary,
        key_points=research.get("key_points", []),
        stats=research.get("stats"),
        sources=research.get("sources"),
        infographic_base64=infographic_base64,
        infographic_url=infographic_url,
    )

    # Save outputs
    html_path = os.path.join(TMP_DIR, "newsletter.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    recipients_path = os.path.join(TMP_DIR, "recipients.txt")
    recipient_list = [r.strip() for r in recipients.split(",")]
    with open(recipients_path, "w") as f:
        f.write("\n".join(recipient_list))

    print(f"\n{'='*50}")
    print("PIPELINE COMPLETE")
    print(f"{'='*50}")
    print(f"HTML:       {html_path}")
    print(f"Recipients: {recipients_path} ({len(recipient_list)} addresses)")
    print(f"\nNext: Agent sends via Gmail MCP")

    return {
        "html_path": html_path,
        "recipients": recipient_list,
        "title": topic,
        "research": research,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage:')
        print('  python tools/run_newsletter.py --research-file .tmp/newsletter_data.json "email1,email2"')
        print('  python tools/run_newsletter.py "Topic" "email1,email2"')
        sys.exit(1)

    if sys.argv[1] == "--research-file":
        # Agent-provided research
        research_file = sys.argv[2]
        recipients = sys.argv[3]
        with open(research_file, encoding="utf-8") as f:
            research = json.load(f)
    else:
        # Fallback: auto-research via OpenRouter
        from tools.research_topic import research_topic

        topic = sys.argv[1]
        recipients = sys.argv[2]
        print(f"Researching '{topic}' via OpenRouter...")
        research = research_topic(topic)

    run_pipeline(research, recipients)
