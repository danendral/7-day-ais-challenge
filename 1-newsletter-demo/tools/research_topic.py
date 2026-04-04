"""
Research a topic using OpenRouter API (fallback when agent can't do research directly).
The primary research method is agent-driven (Claude WebSearch).
This script is the fallback for fully automated runs.

Usage:
    python tools/research_topic.py "Your topic here"
"""

import sys
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"


def research_topic(topic: str) -> dict:
    """Research a topic via OpenRouter (using perplexity/sonar-pro) and return structured results."""
    if not OPENROUTER_API_KEY:
        raise ValueError(
            "OPENROUTER_API_KEY not set in .env. "
            "Either let the agent handle research directly, or add your OpenRouter key."
        )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "perplexity/sonar-pro",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a research assistant for a newsletter. "
                    "Given a topic, provide a comprehensive research summary. "
                    "Return your response as JSON with these keys: "
                    '"title" (catchy newsletter title), '
                    '"summary" (2-3 paragraph overview), '
                    '"key_points" (list of 5-7 bullet points with key insights), '
                    '"stats" (list of relevant statistics or data points), '
                    '"sources" (list of source URLs referenced). '
                    "Be factual, engaging, and concise."
                ),
            },
            {"role": "user", "content": f"Research this topic for a newsletter: {topic}"},
        ],
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()

    data = response.json()
    content = data["choices"][0]["message"]["content"]

    # Try to parse as JSON, fall back to raw text
    try:
        cleaned = content.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1]
            cleaned = cleaned.rsplit("```", 1)[0]
        return json.loads(cleaned)
    except (json.JSONDecodeError, IndexError):
        return {
            "title": topic,
            "summary": content,
            "key_points": [],
            "stats": [],
            "sources": [],
        }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python tools/research_topic.py "Your topic"')
        sys.exit(1)

    topic = " ".join(sys.argv[1:])
    result = research_topic(topic)
    print(json.dumps(result, indent=2))
