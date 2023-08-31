import json
import os
import re


def strip_markdown_links(md_text):
    return re.sub(r'\[(.*?)\]\(.*?\)', r'\1', md_text)


def generate_rich_text_element(text):
    return {
        "type": "rich_text_section",
        "elements": [
            {
                "type": "text",
                "text": strip_markdown_links(text)
            }
        ]
    }


def generate_payload():
    version = os.environ.get("VERSION")
    release_body = os.environ.get("RELEASE_BODY")

    if not version or not release_body:
        raise ValueError("Both VERSION and RELEASE_BODY environment variables must be set and non-empty.")

    bullet_points = release_body.split("\n- ")
    if bullet_points[0].startswith("- "):
        bullet_points[0] = bullet_points[0][2:]

    elements = [generate_rich_text_element(bp) for bp in bullet_points]

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
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_list",
                        "elements": elements,
                        "style": "bullet",
                        "indent": 0
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "A full list of changes are available in the <https://department-of-veterans-affairs.github.io/lighthouse-api-standards/changelog/|change log>."
                }
            }
        ]
    }

    return json.dumps(blocks)


if __name__ == "__main__":
    payload = generate_payload()
    print(f"::set-output name=payload::{payload}")
