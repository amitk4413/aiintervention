import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY missing in .env")

client = OpenAI(api_key=api_key)


def generate_jira_structure(text: str):

    prompt = f"""
You are a STRICT JSON generator for Jira tickets.

Return ONLY valid JSON. No extra text.

RULES:
- Must be valid JSON (json.loads compatible)
- No markdown
- No explanations
- No Python-style objects
- Always close all brackets properly
- Use double quotes only

FORMAT:
{{
  "epics": [
    {{
      "name": "Epic Name",
      "stories": [
        {{
          "type": "user_story",
          "title": "Story title",
          "story": "As a..., I want..., so that...",
          "acceptance_criteria": ["criterion 1", "criterion 2"],
          "epic_link": "Epic Name"
        }}
      ]
    }}
  ]
}}

TEXT:
{text}
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        max_output_tokens=4000
    )

    return response.output_text