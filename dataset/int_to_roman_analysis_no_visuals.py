def int_to_roman(number: int) -> str:
    """
    Converts an integer number to a Roman numeral string representation.

    Args:
        number (int): The integer number to be converted to Roman numeral.

    Returns:
        str: The Roman numeral string representation of the input number.

    Raises:
        ValueError: If the input number is less than 1.

    Example:
        >>> int_to_roman(123)
        'CXXIII'
    """
    num_dict: dict[int, str] = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    roman_numerals: str = ""

    
    if number < 1:
        return "Number must be greater than 1"

    for value in [1000, 500, 100, 50, 10, 5, 1]:
        while number >= value:
            number -= value
            roman_numerals += num_dict[value]
    return roman_numerals
