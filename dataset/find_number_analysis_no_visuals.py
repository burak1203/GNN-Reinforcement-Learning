def find_number(input_string: str) -> int | float | str:
    """
    Finds the first number in the given input string and returns it as an integer or float.

    Args:
        input_string (str): The string to search for a number.

    Returns:
        int or float or str: The first number found in the input string as an integer or float.
        If no number is found, returns "Empty string".
    """
    import re
    from typing import Any

    pattern: str = r"[-+]?[0-9]*\.?[0-9]+"
    matches: list[Any] = re.findall(pattern, input_string)
    if matches:
        input_string = str(input_string)
        number_string = matches[0]
        return int(number_string) if "." not in number_string else float(number_string)
    return "Empty string"
