from crewai import Agent

def TranscriptCleaner(llm):
    return Agent(
        role="Transcript Cleaner",
        goal="Clean messy meeting transcripts",
        backstory="Expert in cleaning meeting notes",
        verbose=True,
        llm=llm
    )