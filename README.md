# Smart Resume Analyzer (Multi-Agent System using Google ADK)

## Architecture

- Root Agent (Orchestrator)
- Resume Parser Agent
- JD Analyzer Agent
- Market Research Agent (google_search tool)
- Keyword Optimizer Agent

## Setup

1. Create virtual environment
   python -m venv .venv
   source .venv/bin/activate (Windows: .venv\Scripts\activate)

2. Install dependencies
   pip install -r requirements.txt

3. Create .env
   GOOGLE_API_KEY=your_key_here

## Run

CLI Mode:
adk run smart_resume_agent
