# AI SDLC Automation

## Overview

AI SDLC Automation is an AI-powered application that converts business requirements into structured Jira Epics and User Stories and automatically creates Jira tickets.

The solution allows users to upload requirement documents in various formats, leverage Large Language Models (LLMs) to analyze the requirements, generate a Jira-ready backlog, and push the generated Epics and Stories directly into Jira.

This helps accelerate the early stages of the Software Development Life Cycle (SDLC) by reducing manual effort involved in requirement analysis and backlog creation.

---

## Features

### Requirement Analysis

* Upload business requirement documents
* Supports:

  * PDF
  * DOCX
  * TXT

### AI-Powered Story Generation

Automatically generates:

* Epics
* User Stories
* Acceptance Criteria

### Jira Integration

Automatically creates:

* Jira Epics
* Jira Stories

inside a configured Jira project.

### Smart Requirement Understanding

The application can understand:

* Formal business requirements
* Meeting notes
* Client discussions
* Layman language requirements
* Semi-structured requirement documents

---

## Architecture

```text
Requirement Document
        │
        ▼
Document Reader
        │
        ▼
OpenAI LLM Analysis
        │
        ▼
Structured Jira JSON
        │
        ▼
Streamlit UI
        │
        ▼
Jira API Integration
        │
        ▼
Jira Epics & Stories
```

---

## Project Structure

```text
ai_agent_sdlc/
│
├── app.py
├── llm_structured.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── tools/
│   └── file_reader.py
│
└── utils/
    ├── json_cleaner.py
    ├── jira_client.py
    └── jira_uploader.py
```

---

## File Descriptions

### app.py

Main Streamlit application.

Responsibilities:

* Upload requirement documents
* Display extracted text
* Trigger AI analysis
* Display generated Jira structure
* Push Epics and Stories to Jira

---

### llm_structured.py

Core AI processing layer.

Responsibilities:

* Send requirements to OpenAI
* Generate structured Jira JSON
* Return Epics, Stories, and Acceptance Criteria

---

### tools/file_reader.py

Document extraction utility.

Responsibilities:

* Read PDF files
* Read DOCX files
* Read TXT files
* Return plain text for AI processing

---

### utils/json_cleaner.py

JSON extraction utility.

Responsibilities:

* Extract valid JSON from LLM responses
* Repair minor formatting issues
* Convert AI output into Python dictionaries

---

### utils/jira_client.py

Low-level Jira API integration.

Responsibilities:

* Create Jira Epics
* Create Jira Stories
* Handle Jira authentication
* Send REST API requests

---

### utils/jira_uploader.py

Jira orchestration layer.

Responsibilities:

* Loop through generated Epics
* Create Epics in Jira
* Create Stories under corresponding Epics

---

## Prerequisites

### Software

* Python 3.10+
* Jira Cloud Account
* OpenAI API Key

### Jira Access

You will need:

* Jira Site URL
* Jira Email
* Jira API Token
* Jira Project Key

---

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

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key

JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your_jira_api_token
JIRA_PROJECT=KAN
```

---

## Running the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will launch automatically in your browser.

---

## Usage

### Step 1

Upload a requirement document:

* PDF
* DOCX
* TXT

---

### Step 2

Click:

```text
Generate Jira Stories
```

The AI will:

* Analyze requirements
* Identify Epics
* Generate User Stories
* Generate Acceptance Criteria

---

### Step 3

Review the generated Jira structure.

Example:

```json
{
  "epics": [
    {
      "name": "Ticket Management",
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

---

### Step 4

Click:

```text
Create Jira Tickets
```

The application automatically creates:

* Jira Epics
* Jira Stories

inside the configured Jira project.

---

## Example Use Cases

### Product Owners

Convert requirements into backlog items.

### Business Analysts

Generate user stories from client requirements.

### Scrum Masters

Accelerate sprint planning preparation.

### Development Teams

Reduce manual effort in backlog creation.

---

## Technologies Used

* Python
* Streamlit
* OpenAI API
* Jira REST API
* Requests
* Python-Dotenv
* PyPDF
* Python-Docx

---

## Future Enhancements

* Story Point Estimation
* Sprint Planning Suggestions
* Priority Classification
* Dependency Detection
* Azure DevOps Integration
* Confluence Integration
* Meeting Transcript Analysis
* Multi-Agent Workflow Support
* RAG-Based Requirement Analysis

---

## Demo Outcome

The solution has been successfully demonstrated with:

* Requirement Upload
* AI Requirement Analysis
* User Story Generation
* Epic Creation
* Automatic Jira Ticket Creation
* Kanban Board Population

---

## Security Notes

* Do not commit `.env` files.
* Do not expose OpenAI API keys.
* Do not expose Jira API tokens.
* Add `.env` to `.gitignore`.

---

## Author

**Amit Kumar**

AI Agent SDLC Framework for enterprise-grade AI solution development and governance.
