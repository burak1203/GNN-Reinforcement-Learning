def word_count(text: str = "") -> int:
    """Calculate the number of words in a given text.

    Args:
        text (str, optional): The input text to be processed.
        Defaults to an empty string. Defaults to "".

    Returns:
        int: The number of words in the input text.
    """

    word_list: list[str] = text.split()
    return len(word_list)
