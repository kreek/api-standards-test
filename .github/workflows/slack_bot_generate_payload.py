import json
import os


def generate_payload():
    version = os.environ.get("VERSION", "N/A")
    release_body = os.environ.get("RELEASE_BODY", "N/A")

    blocks = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":sparkles: *Version {version} of the Lighthouse API Standards has been released:*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": release_body
                }
            }
        ]
    }

    return json.dumps(blocks)


if __name__ == "__main__":
    payload = generate_payload()
    print(f"::set-output name=payload::{payload}")
