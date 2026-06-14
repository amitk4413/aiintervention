import os
import requests
from dotenv import load_dotenv

load_dotenv()

JIRA_DOMAIN = os.getenv("JIRA_BASE_URL")   # ✅ FIXED
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT = os.getenv("JIRA_PROJECT")

if not JIRA_DOMAIN:
    raise ValueError("JIRA_BASE_URL is missing in .env")

AUTH = (JIRA_EMAIL, JIRA_API_TOKEN)

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def create_issue(summary, description, issue_type, epic_key=None):

    url = f"{JIRA_DOMAIN}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT},
            "summary": summary,
            "issuetype": {"name": issue_type}
        }
    }

    # ⚠️ Jira Cloud usually does NOT use "parent" for epic linking
    if epic_key:
        payload["fields"]["parent"] = {"key": epic_key}

    response = requests.post(url, json=payload, headers=HEADERS, auth=AUTH)

    if not response.ok:
        raise Exception(response.text)

    return response.json()


def create_epic(name):

    url = f"{JIRA_DOMAIN}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT},
            "summary": name,
            "issuetype": {"name": "Epic"}
        }
    }

    response = requests.post(url, json=payload, headers=HEADERS, auth=AUTH)

    if not response.ok:
        raise Exception(response.text)

    return response.json()