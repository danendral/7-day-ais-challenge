"""
Send an HTML email via Gmail SMTP with App Password.

Usage:
    python tools/send_email.py "Subject Line" .tmp/newsletter.html "recipient1@email.com,recipient2@email.com"
"""

import sys
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


def send_email(subject: str, html_path: str, recipients: list[str]) -> dict:
    """Send an HTML email to multiple recipients via Gmail SMTP."""
    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        raise ValueError("GMAIL_ADDRESS and GMAIL_APP_PASSWORD must be set in .env")

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    results = {"sent": [], "failed": []}

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)

        for recipient in recipients:
            recipient = recipient.strip()
            try:
                msg = MIMEMultipart("alternative")
                msg["From"] = GMAIL_ADDRESS
                msg["To"] = recipient
                msg["Subject"] = subject
                msg.attach(MIMEText(html_content, "html"))

                server.sendmail(GMAIL_ADDRESS, recipient, msg.as_string())
                results["sent"].append(recipient)
                print(f"  Sent to {recipient}")
            except Exception as e:
                results["failed"].append({"recipient": recipient, "error": str(e)})
                print(f"  Failed for {recipient}: {e}")

    return results


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('Usage: python tools/send_email.py "Subject" path/to/email.html "email1,email2"')
        sys.exit(1)

    subject = sys.argv[1]
    html_path = sys.argv[2]
    recipients = [r.strip() for r in sys.argv[3].split(",")]

    print(f"Sending '{subject}' to {len(recipients)} recipient(s)...")
    results = send_email(subject, html_path, recipients)
    print(f"\nDone: {len(results['sent'])} sent, {len(results['failed'])} failed")
