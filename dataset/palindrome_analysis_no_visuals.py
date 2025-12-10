def palindrome(string: str = "") -> None:
    """
    Check if a given string is a palindrome.

    Parameters:
        string (str): The string to be checked.

    Returns:
        None
    """
    string = str(string)
    if string == string[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
