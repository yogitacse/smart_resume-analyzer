def save_report(content: str, filename: str = "resume_report.md") -> str:
    """
    Saves markdown report to file.
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Report saved as {filename}"
