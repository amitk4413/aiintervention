from crewai import Agent


def create_agents(llm):

    return {
        "cleaner": Agent(
            role="Cleaner",
            goal="Clean raw meeting text",
            backstory="Expert in cleaning transcripts",
            llm=llm,
            verbose=True
        ),

        "extractor": Agent(
            role="Extractor",
            goal="Extract structured requirements",
            backstory="Business analyst expert",
            llm=llm,
            verbose=True
        ),

        "story": Agent(
            role="Jira Story Writer",
            goal="Convert requirements into STRICT JSON format",
            backstory="Expert Jira formatter",
            llm=llm,
            verbose=True
        ),

        "validator": Agent(
            role="JSON Validator",
            goal="Ensure output is valid JSON only",
            backstory="Strict JSON checker",
            llm=llm,
            verbose=True
        )
    }