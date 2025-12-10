def count_string_characters_and_digits(txt: str = "") -> None:
    """
    Count the number of alphabets, digits, and special characters in a given string.
    Parameters:
        txt (str): The input string to count characters and digits from.
    Returns:
        None
    """
    if type(txt) is not str:
        txt = str(txt)

    alphabets = digits = special = 0
    for i in range(len(txt)):
        if txt[i].isalpha():
            alphabets = alphabets + 1
        elif txt[i].isdigit():
            digits = digits + 1
        else:
            special = special + 1

    print("\nTotal Number of Alphabets in this String : ", alphabets)
    print("Total Number of Digits in this String : ", digits)
    print("Total Number of Special Characters in this String : ", special)
