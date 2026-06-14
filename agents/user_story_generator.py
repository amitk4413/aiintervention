from crewai import Agent

def UserStoryGenerator(llm):
    return Agent(
        role="User Story Writer",
        goal="Convert requirements into Jira user stories",
        backstory="Agile expert",
        verbose=True,
        llm=llm
    )