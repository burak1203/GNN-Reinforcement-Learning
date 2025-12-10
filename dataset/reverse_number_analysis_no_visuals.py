def reverse_number(number: int) -> None:
    """
    Reverses a given number and prints it.

    Parameters:
        number (int): The number to be reversed.

    Returns:
        None:

    Example:
        >>> reverse_number(12)
        21
    """
    reverse: int = 0
    while number > 0:
        digit: int = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    print("Reverse of the number:", reverse)
