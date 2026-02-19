from google.adk.agents import LlmAgent

keyword_optimizer_agent = LlmAgent(
    name="KeywordOptimizerAgent",
    model="gemini-1.5-flash-8b" ,
    description="Compare resume skills with job description and suggest keyword improvements.",
)
