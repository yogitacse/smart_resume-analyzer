from google.adk.agents import LlmAgent

market_research_agent = LlmAgent(
    name="MarketResearchAgent",
    model="gemini-1.5-flash-8b" ,
    description="Research current in-demand skills related to the job role.",
)
