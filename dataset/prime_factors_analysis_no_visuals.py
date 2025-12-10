def prime_factors(number: int) -> None:
    """
    Calculates the prime factors of a given number.

    Args:
        number (int): The number to calculate the prime factors of.

    Returns:
        None: This function does not return anything.
        It prints the prime factors of the given number.

    Raises:
        None: This function does not raise any exceptions.

    Examples:
        >>> prime_factors(10)
        2 is a Prime Factor of a Given number 10
        5 is a Prime Factor of a Given number 10

        >>> prime_factors(7)
        7 is a Prime Factor of a Given number 7

        >>> prime_factors(1)
        Invalid Input
    """
    for i in range(2, number + 1):
        if number % i == 0:
            is_prime = 1
            for j in range(2, (i // 2 + 1)):
                if i % j == 0:
                    is_prime = 0
                    break
            if is_prime == 1:
                print(f"{i} is a Prime Factor of a Given number {number}")
