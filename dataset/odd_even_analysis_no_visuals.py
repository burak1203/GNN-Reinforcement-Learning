def odd_even(number: int) -> str:
    """
    Checks if the given number is odd or even.

    Args:
        number (int): The number to check.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.
        If the input is not an integer, returns "Please enter a number”.
    """

    if number % 2 == 0:
        return "Even"
    return "Odd"