def find_divisors(number: int) -> None:
    """
    Finds all divisors of a given number.

    Args:
        number (int): The number to find divisors for.
    """
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
