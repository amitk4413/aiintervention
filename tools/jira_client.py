import requests
import os

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT = os.getenv("JIRA_PROJECT")


def auth():
    return (JIRA_EMAIL, JIRA_API_TOKEN)


def headers():
    return {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }


# =========================
# CREATE EPIC
# =========================
def create_epic(epic_name):

    url = f"{JIRA_BASE_URL}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT},
            "summary": epic_name,
            "issuetype": {"name": "Epic"}
        }
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers(),
        auth=auth()
    )

    if response.status_code != 201:
        print("JIRA ERROR:", response.text)
        response.raise_for_status()

    return response.json()["key"]