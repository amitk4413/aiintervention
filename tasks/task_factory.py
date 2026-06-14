from crewai import Task


def create_tasks(agents, text):

    t1 = Task(
        description=f"""
Clean the document and remove noise.

TEXT:
{text}
""",
        expected_output="clean cleaned text",
        agent=agents["cleaner"]
    )

    t2 = Task(
        description="""
Extract structured requirements from the cleaned text.
Group into meaningful business requirements.
""",
        expected_output="structured requirement list",
        agent=agents["extractor"],
        context=[t1]
    )

    t3 = Task(
        description="""
Convert requirements into STRICT VALID JSON.

RULES:
- Output ONLY JSON
- NO markdown
- NO explanations
- NO Python dict format (NO 0:, NO 1:)
- ALL keys must be double quoted

FORMAT:
{
  "epics": [
    {
      "name": "Epic Name",
      "stories": [
        {
          "type": "user_story",
          "title": "Title",
          "story": "Story",
          "acceptance_criteria": ["A", "B"],
          "epic_link": "Epic Name"
        }
      ]
    }
  ]
}
""",
        expected_output="VALID JSON ONLY",
        agent=agents["story"],
        context=[t2]
    )

    t4 = Task(
        description="""
Validate and fix JSON.

Rules:
- Must return VALID JSON ONLY
- Fix formatting issues if any
- Remove any extra text or markdown
""",
        expected_output="clean valid JSON",
        agent=agents["validator"],
        context=[t3]
    )

    return [t1, t2, t3, t4]