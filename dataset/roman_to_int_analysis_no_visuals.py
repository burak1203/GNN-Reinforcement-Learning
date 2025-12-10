def roman_to_int(roman_number: str) -> int:
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_number (str): The Roman numeral to be converted.

    Returns:
        int: The integer representation of the Roman numeral.

    Raises:
        None

    Examples:
        >>> roman_to_int("MMXXIIII")
        2024
        >>> roman_to_int("")
        Empty string. Please enter a valid roman number.
        0

    Note:
        The function assumes that the input string is a valid Roman numeral.
        If the input string is empty, it prints a message and returns None.
    """
    total = 0

    if roman_number:
        roman_dict: dict[str, int] = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in range(len(roman_number) - 1):
            if roman_dict[roman_number[i]] >= roman_dict[roman_number[i + 1]]:
                total += roman_dict[roman_number[i]]
            else:
                total -= roman_dict[roman_number[i]]
        total += roman_dict[roman_number[-1]]
    else:
        print("Empty string. Please enter a valid roman number.")
    return total
