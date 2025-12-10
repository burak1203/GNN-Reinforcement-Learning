def perfect_number(number: int) -> bool:
    """
    Check if a given number is a perfect number.

    Parameters:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a perfect number, False otherwise.
    """

    counter: int = 0

    for i in range(1, number):
        if number % i == 0:
            counter += i

    if counter == number:
        return True
    return False
