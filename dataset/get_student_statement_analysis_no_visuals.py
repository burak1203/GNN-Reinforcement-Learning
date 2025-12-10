def get_student_statement(score: float) -> str:
    """
    Generates a student statement based on the given score.

    Args:
        score (float): The score of the student.

    Returns:
        str: The student statement based on the score.
            - "AA" if the score is between 95 and 100 (inclusive).
            - "BB" if the score is between 90 and 95 (inclusive).
            - "BC" if the score is between 80 and 90 (inclusive).
            - "CC" if the score is between 70 and 80 (inclusive).
            - "DC" if the score is between 60 and 70 (inclusive).
            - "DD" if the score is between 50 and 60 (inclusive).
            - "FF" if the score is between 0 and 50 (inclusive).
            - "invalid score" if the score is outside the valid range.
    """

    if 100 >= score and score >= 95:
        return "AA"
    elif 95 > score and score >= 90:
        return "BB"
    elif 90 > score and score >= 80:
        return "BC"
    elif 80 > score and score >= 70:
        return "CC"
    elif 70 > score and score >= 60:
        return "DC"
    elif 60 > score and score >= 50:
        return "DD"
    elif 50 > score and score >= 0:
        return "FF"
    else:
        return "invalid score"
