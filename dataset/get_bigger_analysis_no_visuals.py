def get_bigger(first_number: float, second_number: float) -> str:
    """
    Determines which of two numbers is bigger and returns a string indicating the result.

    Args:
        first_number (float): The first number.
        second_number (float): The second number.

    Returns:
        str: A string indicating the result of the comparison. Possible values are:
            - "first_number < b" if first_number is less than second_number.
            - "first_number = b" if first_number is equal to second_number.
            - "first_number > b" if first_number is greater than second_number.
            - "first_number < 5" if a is less than 5.
    """

    if first_number < second_number:
        if first_number < 5:
            return "first_number < 5"
        return "first_number < second_number"

    elif first_number == second_number:
        return "first_number = second_number"

    else:
        return "first_number > second_number"