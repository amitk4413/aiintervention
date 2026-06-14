from crewai import Agent

def RequirementExtractor(llm):
    return Agent(
        role="Requirement Analyst",
        goal="Extract structured requirements",
        backstory="Business analyst expert",
        verbose=True,
        llm=llm
    )