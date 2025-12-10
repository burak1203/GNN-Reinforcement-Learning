def print_multiplier(number: int) -> None:
    """
    Prints the factors of a given integer number.

    Args:
        number (int): The integer number to find the factors of.

    Returns:
        None: This function does not return anything.

    Raises:
        None: This function does not raise any exceptions.

    Examples:
        >>> print_multiplier(2)
        The factors of 2 are:
        1
        2
    """

    if number < 0:
        print("Take a positive number")
    else:
        print("The factors of", number, "are:")
        for i in range(1, number + 1):
            if number % i == 0:
                print(i)
