def prime_number(number: int) -> str:
    """
    Determines whether a given number is prime or not.

    Args:
        number (int): The number to check for primality.

    Returns:
        str: Returns "Prime Number" if the number is prime, otherwise returns "Not Prime Number".
    """
    prime: bool = True
    divisor: int = 0

    if number < 2 or number % 2 == 0:
        return "Not Prime Number"

    for i in range(1, number + 1):
        if number % i == 0:
            divisor += 1

        if divisor > 2:
            prime = False
            break

    if prime:
        return "Prime Number"
    else:
        return "Not Prime Number "
