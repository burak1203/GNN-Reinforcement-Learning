def check_email(txt: str) -> None:
    """
    Check if the given string is a valid email address.

    Args:
        txt (str): The string to be checked.

    Returns:
        None: This function does not return anything.
        It prints "Valid Email" if the string is a valid email address,
        and "Invalid Email" otherwise.

    Raises:
        None

    Examples:
        >>> check_email("example@example.com")
        Valid Email
        >>> check_email("invalid_email")
        Invalid Email
    """
    import re

    # Make a regular expression
    # for validating an Email
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    # Define a function for
    # for validating an Email
    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, txt):
        print("Valid Email")
    else:
        print("Invalid Email")
