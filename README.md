# AI SDLC Automation

AI-powered solution that converts business requirements into structured Jira Epics and User Stories, and automatically creates Jira tickets.

## Overview

AI SDLC Automation streamlines the Software Development Life Cycle (SDLC) by leveraging Large Language Models (LLMs) to analyze requirement documents and generate Jira-ready backlog items.

The application accepts requirement documents in multiple formats, extracts key business needs, generates Epics and User Stories with acceptance criteria, and optionally pushes them directly into Jira.

## Features

* Upload requirement documents (PDF, DOCX, TXT)
* Extract and analyze business requirements using AI
* Generate:

  * Epics
  * User Stories
  * Technical Stories
  * Acceptance Criteria
* Organize stories under appropriate Epics
* Create Jira Epics and Stories automatically
* Streamlit-based user interface
* Support for unstructured and layman-language requirements

## Architecture

```text
Requirement Document
        │
        ▼
Document Reader
        │
        ▼
AI Analysis Engine
        │
        ▼
Structured Jira JSON
        │
        ├── Display in Streamlit
        │
        └── Push to Jira
                │
                ▼
          Jira Epics & Stories
```

## Project Structure

```text
ai_agent_sdlc/
│
├── app.py
├── llm_structured.py
│
├── agents/
├── crews/
├── tasks/
├── tools/
├── utils/
│
├── requirements.txt
├── .env
└── README.md
```

## Prerequisites

* Python 3.10+
* OpenAI API Key
* Jira Cloud Account
* Jira API Token

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ai_agent_sdlc
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_key

JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your_email@example.com
JIRA_API_TOKEN=your_jira_api_token
JIRA_PROJECT=KAN
```

## Running the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

## Usage

### Step 1 – Upload Requirement Document

Upload a:

* PDF
* DOCX
* TXT

document containing business requirements.

### Step 2 – Generate Jira Structure

Click:

```text
Generate Jira Stories
```

The AI will:

* Analyze requirements
* Identify Epics
* Generate User Stories
* Create Acceptance Criteria

### Step 3 – Review Output

Generated Jira structure is displayed as JSON.

Example:

```json
{
  "epics": [
    {
      "name": "Customer Support Ticketing System",
      "stories": [
        {
          "title": "Create Support Tickets",
          "type": "user_story"
        }
      ]
    }
  ]
}
```

### Step 4 – Push to Jira

Click:

```text
Push to Jira
```

The application creates:

* Jira Epics
* Jira Stories

inside the configured Jira project.

## Supported Requirement Formats

The AI can process:

### Structured Requirements

```text
As a user, I want...
```

### Meeting Notes

```text
Need ticket creation on web and mobile.
Send notifications when status changes.
```

### Layman Language

```text
Customers should be able to raise issues from mobile phones.
Support team should get notified.
```

## Example Use Cases

* Requirement Engineering
* Agile Backlog Creation
* Jira Automation
* Product Discovery Workshops
* Business Analysis
* Sprint Planning Preparation

## Future Enhancements

* Story Point Estimation
* Sprint Recommendation
* Priority Assignment
* Dependency Mapping
* Azure DevOps Integration
* Confluence Integration
* RAG-based Requirement Analysis
* Multi-Agent SDLC Workflow

## Demo

The project has been successfully demonstrated with:

* Requirement Upload
* AI Story Generation
* Automatic Jira Ticket Creation
* Kanban Board Population

## Author

Amit Kumar

AI SDLC Automation Prototype
