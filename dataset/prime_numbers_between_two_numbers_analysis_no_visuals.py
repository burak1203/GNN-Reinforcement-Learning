def prime_numbers_between_two_numbers(lower: int, upper: int) -> None:
    """
    Generates prime numbers between the given lower and upper bounds.

    Parameters:
        lower (int): The lower bound of the range.
        upper (int): The upper bound of the range.

    Returns:
        None

    Raises:
        None

    Prints:
        Prime numbers between the lower and upper bounds.

    Example:
        >>> prime_numbers_between_two_numbers(1, 10)
        Prime numbers between 1 and 10 are:
        2
        3
        5
        7
    """

    if lower < 1 or upper < 1:
        print("Please input positive integer values only")

    else:
        print("Prime numbers between", lower, "and", upper, "are:")

        for num in range(lower, upper + 1):
            # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)
