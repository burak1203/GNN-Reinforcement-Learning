def factorial(value: int) -> int:
    """
    Calculates the factorial of a given integer value.

    Args:
        value (int): The integer value for which the factorial needs to be calculated.

    Returns:
        int: The factorial of the given value.

    Raises:
        None

    Examples:
        >>> factorial(5)
        120
        >>> factorial(1)
        1
        """
    if value  == 1:
        return 1

    return value * factorial(value - 1)
