def positive_divisors(number: int) -> None:
    """
    Calculates and prints the number of positive divisors of a given number.

    Parameters:
        number (int): The number for which to calculate the positive divisors.

    Returns:
        None

    Raises:
        None
    """
    if number < 0:
        print("Please enter a positive number")

    else:
        counter: int = 0

        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
                print(i)

        print(f"Number of positive divisors: {counter}")
