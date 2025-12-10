def decimal_to_binary(decimal: int) -> str:
    """
    Convert a decimal number to its binary representation.

    Args:
        decimal (int): The decimal number to be converted.

    Returns:
        str: The binary representation of the decimal number.

    This function takes an integer as input and converts it to its binary representation.
    It iteratively divides the decimal number by 2 and appends the remainder (0 or 1) to the binary string.
    The process continues until the decimal number becomes 0. The resulting binary string is then returned.

    Example:
        >>> decimal_to_binary(11)
    '        1011'
    """
    binary: str = ""
    while decimal:
        binary = "01"[decimal & 1] + binary
        decimal >>= 1

    return binary
