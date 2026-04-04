"""
Format newsletter content into a responsive HTML email.
Takes research data and optional infographic, outputs HTML string.

Usage:
    python tools/format_newsletter.py  (reads from .tmp/newsletter_data.json)
"""

import sys
import os
import json
from datetime import datetime

TMP_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".tmp")


def format_newsletter(
    title: str,
    summary: str,
    key_points: list[str],
    stats: list[str] = None,
    sources: list[str] = None,
    infographic_base64: str = None,
    infographic_url: str = None,
) -> str:
    """Generate HTML email from newsletter content."""

    date_str = datetime.now().strftime("%B %d, %Y")

    key_points_html = "\n".join(
        f'<li style="margin-bottom:8px;color:#333333;font-size:15px;line-height:1.6;">{point}</li>'
        for point in key_points
    )

    stats_html = ""
    if stats:
        stats_items = "\n".join(
            f'<li style="margin-bottom:6px;color:#555555;font-size:14px;">{stat}</li>'
            for stat in stats
        )
        stats_html = f"""
        <div style="background:#f0f4ff;border-left:4px solid #4a90d9;padding:16px 20px;margin:24px 0;border-radius:0 8px 8px 0;">
            <h3 style="margin:0 0 12px 0;color:#4a90d9;font-size:16px;">Key Stats</h3>
            <ul style="margin:0;padding-left:20px;">{stats_items}</ul>
        </div>"""

    infographic_html = ""
    # Prefer hosted URL (email clients block base64), fall back to base64
    img_src = None
    if infographic_url:
        img_src = infographic_url
    elif infographic_base64:
        img_src = f"data:image/png;base64,{infographic_base64}"

    if img_src:
        infographic_html = f"""
        <div style="text-align:center;margin:24px 0;">
            <img src="{img_src}"
                 alt="Newsletter Infographic"
                 style="max-width:100%;height:auto;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1);" />
        </div>"""

    sources_html = ""
    if sources:
        source_links = "\n".join(
            f'<li style="margin-bottom:4px;"><a href="{src}" style="color:#4a90d9;font-size:13px;text-decoration:none;">{src}</a></li>'
            for src in sources
        )
        sources_html = f"""
        <div style="margin-top:24px;padding-top:16px;border-top:1px solid #e0e0e0;">
            <h3 style="color:#888888;font-size:13px;text-transform:uppercase;letter-spacing:1px;">Sources</h3>
            <ul style="padding-left:20px;margin:8px 0;">{source_links}</ul>
        </div>"""

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background-color:#f5f5f5;font-family:Arial,Helvetica,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f5f5f5;">
<tr><td align="center" style="padding:20px 10px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.08);">

    <!-- Header -->
    <tr><td style="background:linear-gradient(135deg,#4a90d9,#7b68ee);padding:32px 40px;text-align:center;">
        <h1 style="margin:0;color:#ffffff;font-size:26px;font-weight:700;line-height:1.3;">{title}</h1>
        <p style="margin:8px 0 0;color:rgba(255,255,255,0.85);font-size:14px;">{date_str}</p>
    </td></tr>

    <!-- Body -->
    <tr><td style="padding:32px 40px;">

        <!-- Summary -->
        <div style="color:#333333;font-size:15px;line-height:1.7;margin-bottom:24px;">
            {summary}
        </div>

        {infographic_html}

        <!-- Key Points -->
        <h2 style="color:#2c3e50;font-size:18px;margin:24px 0 12px;border-bottom:2px solid #4a90d9;padding-bottom:8px;">
            Key Takeaways
        </h2>
        <ul style="padding-left:20px;margin:0;">
            {key_points_html}
        </ul>

        {stats_html}
        {sources_html}

    </td></tr>

    <!-- Footer -->
    <tr><td style="background-color:#f9f9f9;padding:20px 40px;text-align:center;border-top:1px solid #eeeeee;">
        <p style="margin:0;color:#999999;font-size:12px;">
            Generated with AI-powered research and design
        </p>
    </td></tr>

</table>
</td></tr>
</table>
</body>
</html>"""

    return html


if __name__ == "__main__":
    data_path = os.path.join(TMP_DIR, "newsletter_data.json")
    if not os.path.exists(data_path):
        print(f"No data file found at {data_path}")
        print("Run research_topic.py first, then save output to .tmp/newsletter_data.json")
        sys.exit(1)

    with open(data_path) as f:
        data = json.load(f)

    html = format_newsletter(
        title=data.get("title", "Newsletter"),
        summary=data.get("summary", ""),
        key_points=data.get("key_points", []),
        stats=data.get("stats"),
        sources=data.get("sources"),
        infographic_base64=data.get("infographic_base64"),
    )

    output_path = os.path.join(TMP_DIR, "newsletter.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Newsletter HTML saved to {output_path}")
