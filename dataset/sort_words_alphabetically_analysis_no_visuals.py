def sort_words_alphabetically(text: str) -> None:
    """
    Sorts the words in the given text alphabetically and prints them.

    Args:
        text (str): The text to be sorted.

    Returns:
        None
    """
    text_split: list[str] = text.split()
    text_split.sort()

    print("Alphabetical order:")
    for x in text_split:
        print(x)
