from google.adk.agents import LlmAgent

jd_analyzer_agent = LlmAgent(
    name="JDAnalyzerAgent",
    model="gemini-1.5-flash-8b",
    description="Analyze job description and extract required skills and responsibilities.",
)
