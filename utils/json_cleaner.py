import json
import re

def extract_json(text: str):
    """
    Safely extracts valid JSON from LLM output.
    Fixes common issues like markdown, truncation noise, etc.
    """

    if not text:
        raise ValueError("Empty response from LLM")

    # Remove markdown fences if any
    text = text.replace("```json", "").replace("```", "")

    # First try direct parsing
    try:
        return json.loads(text)
    except Exception:
        pass

    # Extract JSON block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in LLM output")

    return json.loads(match.group(0))