from crewai import Crew
from tasks.task_factory import create_tasks
from agents.agent_factory import create_agents
import json
import re


def force_extract_json(text: str):

    # remove markdown if any
    text = text.replace("```json", "").replace("```", "")

    # extract biggest JSON block
    start = text.find("{")
    end = text.rfind("}") + 1
    if start != -1 and end != -1:
        text = text[start:end]

    # 🚨 CRITICAL FIX: convert Python dict style → JSON

    # 0:{ → "0":{
    text = re.sub(r'(\n|\{|\[)\s*(\d+)\s*:', r'\1"\2":', text)

    # convert keys without quotes: name: → "name":
    text = re.sub(r'([a-zA-Z_]+)\s*:', r'"\1":', text)

    return text


def run_crew(llm, text):

    agents = create_agents(llm)
    tasks = create_tasks(agents, text)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process="sequential",
        verbose=True,
        memory=False
    )

    result = crew.kickoff()

    raw = str(result)

    cleaned = force_extract_json(raw)

    try:
        parsed = json.loads(cleaned)
        return parsed

    except Exception:

        return {
            "raw": raw,
            "error": "LLM output not valid JSON even after full repair",
            "hint": "Switch to structured outputs (recommended next step)"
        }