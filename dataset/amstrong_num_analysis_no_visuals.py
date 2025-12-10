def amstrong_num(number: int) -> None:
    """
    A function to determine if a number is an Armstrong number.

    Parameters:
        number (int): The number to be checked for Armstrong property.

    Returns:
        None
    """
    # Changed num variable to string
    number_str: str = str(number)

    # initialize sum
    total: int = 0

    # find the sum of the cube of each digit
    for i in number_str:
        total += int(i) ** 3

    # Change number variable to int
    number = int(number_str)

    # display the result
    if number == total:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")
