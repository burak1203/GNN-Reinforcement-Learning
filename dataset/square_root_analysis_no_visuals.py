def square_root(number: int) -> None:
    """
    Calculate the square root of a positive integer and print the result.

    Args:
        number (int): The positive integer for which the square root is to be calculated.

    Returns:
        None: This function does not return anything. It prints the square root of the input number.

    Raises:
        None: This function does not raise any exceptions.

    Example:
        >>> square_root(4)
        2.0
        >>> square_root(-1)
        please enter a positive integer
    """
    
    print(number**0.5)
