from utils.jira_client import create_epic, create_issue

def push_to_jira(data):

    results = []

    for epic in data.get("epics", []):

        epic_name = epic["name"]
        epic_resp = create_epic(epic_name)
        epic_key = epic_resp["key"]

        for story in epic.get("stories", []):

            summary = story["title"]
            description = story.get("story", "")
            issue_type = "Task"

            issue_resp = create_issue(
                summary=summary,
                description=description,
                issue_type=issue_type,
                epic_key=epic_key
            )

            results.append(issue_resp)

    return results