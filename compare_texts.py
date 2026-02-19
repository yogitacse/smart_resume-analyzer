def compare_texts(resume_text: str, jd_text: str) -> dict:
    """
    Compares resume and job description and returns missing keywords.

    Args:
        resume_text (str)
        jd_text (str)

    Returns:
        dict: Matching and missing keywords
    """

    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())

    matching = resume_words.intersection(jd_words)
    missing = jd_words.difference(resume_words)

    return {
        "matching_keywords": list(matching),
        "missing_keywords": list(missing)
    }
