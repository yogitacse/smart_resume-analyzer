# Problem Statement: Smart Resume Analyzer

Build a multi-agent system that:

1. Accepts a Resume (PDF)
2. Accepts a Job Description (text)
3. Extracts key skills from both
4. Compares resume with job description
5. Identifies missing keywords
6. Uses Google Search to identify trending industry skills
7. Suggests improvements
8. Generates a structured Markdown improvement report

Architecture:

- Root Agent (Orchestrator)
- Resume Parser Agent
- JD Analyzer Agent
- Market Research Agent (uses google_search)
- Keyword Optimizer Agent

Pattern Used:
Sequential + Parallel
