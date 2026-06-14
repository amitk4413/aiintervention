from crewai import Agent

def JiraValidator(llm):
    return Agent(
        role="Jira Validator",
        goal="Validate Jira format stories",
        backstory="Jira admin expert",
        verbose=True,
        llm=llm
    )