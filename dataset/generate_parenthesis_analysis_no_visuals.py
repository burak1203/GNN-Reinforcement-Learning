def generate_parenthesis(number: int) -> list[str]:
    """
    Generates all possible combinations of well-formed parentheses of length `number`.

    Parameters:
        number (int): The length of the well-formed parentheses.

    Returns:
        list: A list of strings representing all possible combinations of well-formed parentheses.

    Example:
        >>> generate_parenthesis(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
    """

    result: list[str] = []

    def backtrack(S: str, open_count: int, close_count: int, result: list[str]) -> None:
        if len(S) == 2 * number:
            result.append(S)
            return
        if open_count < number:
            backtrack(S + "(", open_count + 1, close_count, result)
        if close_count < open_count:
            backtrack(S + ")", open_count, close_count + 1, result)

    backtrack("", 0, 0, result)
    return result
