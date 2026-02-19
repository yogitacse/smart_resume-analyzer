from google.adk.agents import LlmAgent
from smart_resume_agent.tools.extract_pdf_text import extract_pdf_text

resume_parser_agent = LlmAgent(
    name="ResumeParserAgent",
    model="gemini-1.5-flash-8b",
    description="Extract text from resume PDF and summarize candidate skills.",
    tools=[extract_pdf_text],
)
