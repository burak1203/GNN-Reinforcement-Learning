def reverse_string(txt: str) -> None:
    """
    Reverses the given string and prints the original and reversed strings.

    Args:
        txt (str): The string to be reversed.

    Returns:
        None
    """

    reverse: str = txt[::-1]

    print("\n-----\n")
    print("Original = ", txt)
    print("Reversed =", reverse)
