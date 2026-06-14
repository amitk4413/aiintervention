from tools.jira_client import JiraClient


class JiraConverter:

    def __init__(self):
        self.client = JiraClient()

    def convert(self, data):

        created_issues = []

        for epic in data.get("epics", []):

            # 1️⃣ Create Epic
            epic_issue = self.client.create_issue(
                summary=epic["name"],
                description=f"Auto-created Epic: {epic['name']}",
                issue_type="Epic",
                labels=["ai-generated", "epic"]
            )

            epic_key = epic_issue["key"]

            # 2️⃣ Create Stories under Epic
            for story in epic["stories"]:

                desc = self.format_story(story)

                issue = self.client.create_issue(
                    summary=story["title"],
                    description=desc,
                    issue_type="Task",
                    epic_key=epic_key,
                    labels=[story.get("type", "user_story")]
                )

                created_issues.append(issue["key"])

        return created_issues

    def format_story(self, story):

        ac = "\n".join([f"- {c}" for c in story.get("acceptance_criteria", [])])

        return f"""
User Story:
{story['story']}

Acceptance Criteria:
{ac}
"""