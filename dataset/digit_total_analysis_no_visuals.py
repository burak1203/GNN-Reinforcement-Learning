def digit_total(number: int) -> int:
    """
    Calculate the sum of the digits of a given integer.

    Args:
        number (int): The integer whose digits are to be summed.

    Returns:
        int: The sum of the digits of the given integer.
    """
    
    total: int = 0

    while number != 0:
        total += number % 10
        number = number // 10

    return total
