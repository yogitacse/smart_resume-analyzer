import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

from smart_resume_agent.sub_agents.resume_parser_agent import resume_parser_agent
from smart_resume_agent.sub_agents.jd_analyzer_agent import jd_analyzer_agent
from smart_resume_agent.sub_agents.market_research_agent import market_research_agent
from smart_resume_agent.sub_agents.keyword_optimizer_agent import keyword_optimizer_agent

load_dotenv()

root_agent = LlmAgent(
    name="SmartResumeOrchestrator",
    model="gemini-1.5-flash-latest" 
,
    description="Coordinates resume parsing, job description analysis, market research and optimization.",
    sub_agents=[
        resume_parser_agent,
        jd_analyzer_agent,
        market_research_agent,
        keyword_optimizer_agent,
    ],
)
