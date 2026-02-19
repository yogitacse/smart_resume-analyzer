def generate_markdown_report(data: dict) -> str:
    """
    Generates a structured markdown improvement report.
    """

    report = f"""
# Resume Optimization Report

## Matching Keywords
{', '.join(data.get("matching_keywords", []))}

## Missing Keywords
{', '.join(data.get("missing_keywords", []))}

## Market Trends
{data.get("market_trends", "")}

## Suggested Improvements
{data.get("suggestions", "")}
"""

    return report
