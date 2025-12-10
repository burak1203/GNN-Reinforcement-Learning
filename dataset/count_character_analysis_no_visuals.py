def count_character(txt: str) -> None:
    """
    A function that counts the total number of characters in a given string.

    Parameters:
        txt (str): The input string to count characters from.

    Returns:
        None
    """
    total: int = 0

    for _ in txt:
        total = total + 1

    print("Total Number of Characters in this String = ", total)
