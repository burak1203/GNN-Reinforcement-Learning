def length(_str: str) -> None:
    """
    Calculates the length of a given string and prints it.

    Parameters:
        _str (str): The string whose length is to be calculated.

    Returns:
        None

    Example:
        >>> length("123")
        3

        >>> length(123)
        3
    """
    _len: int = 0

    if type(_str) is str:
        _str = str(_str)
        _len = len(_str)
        print(f"{_str}: {_len}")

    else:
        _len = len(_str)
        print(f"{_str} : {_len}")
