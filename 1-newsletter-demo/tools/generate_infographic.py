"""
Generate an infographic image using the Nano Banana API.
Returns the path to the saved image and its base64 encoding.

Usage:
    python tools/generate_infographic.py "A visual description of the infographic"
"""

import sys
import os
import json
import time
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

NANOBANANA_API_KEY = os.getenv("NANOBANANA_API_KEY")
GENERATE_URL = "https://api.nanobananaapi.ai/api/v1/nanobanana/generate"
STATUS_URL = "https://api.nanobananaapi.ai/api/v1/nanobanana/record-info"
TMP_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".tmp")


def generate_infographic(prompt: str, image_size: str = "16:9") -> dict:
    """Generate an infographic and return image path + base64."""
    if not NANOBANANA_API_KEY:
        raise ValueError("NANOBANANA_API_KEY not set in .env")

    os.makedirs(TMP_DIR, exist_ok=True)

    headers = {
        "Authorization": f"Bearer {NANOBANANA_API_KEY}",
        "Content-Type": "application/json",
    }

    # Submit generation task
    payload = {
        "prompt": prompt,
        "type": "TEXTTOIAMGE",
        "numImages": 1,
        "image_size": image_size,
        "callBackUrl": "https://example.com/noop",  # Required but we poll instead
    }

    response = requests.post(GENERATE_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    task_id = response.json()["data"]["taskId"]
    print(f"Task submitted: {task_id}")

    # Poll for completion
    for attempt in range(60):  # Max ~5 minutes
        time.sleep(5)
        status_resp = requests.get(
            STATUS_URL,
            params={"taskId": task_id},
            headers={"Authorization": f"Bearer {NANOBANANA_API_KEY}"},
            timeout=15,
        )
        status_resp.raise_for_status()
        status_data = status_resp.json()["data"]

        if status_data.get("successFlag") == 1:
            image_url = status_data["response"]["resultImageUrl"]
            print(f"Image ready: {image_url}")

            # Download image
            img_resp = requests.get(image_url, timeout=30)
            img_resp.raise_for_status()

            image_path = os.path.join(TMP_DIR, f"infographic_{task_id}.png")
            with open(image_path, "wb") as f:
                f.write(img_resp.content)

            img_base64 = base64.b64encode(img_resp.content).decode("utf-8")

            return {
                "image_path": image_path,
                "image_base64": img_base64,
                "image_url": image_url,
            }

        if status_data.get("errorCode") and status_data["errorCode"] != 0:
            raise RuntimeError(
                f"Image generation failed: {status_data.get('errorMessage', 'Unknown error')}"
            )

        print(f"  Polling... attempt {attempt + 1}")

    raise TimeoutError("Image generation timed out after 5 minutes")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python tools/generate_infographic.py "description"')
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    result = generate_infographic(prompt)
    print(f"Saved to: {result['image_path']}")
    print(f"Base64 length: {len(result['image_base64'])} chars")
