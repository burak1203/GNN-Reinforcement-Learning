def pop_letter(value: str, way: int) -> None:
    """
    Prints a sequence of letters in a string, each on its own line, in a way that is determined by the value of the way parameter.
    If way is 1, prints each letter from the beginning of the string to the end of the string, one line at a time.
    If way is 2, prints each letter from the beginning of the string to the end of the string and back to the beginning of the string, one line at a time.
    It raises a ValueError if a way other than 1 or 2 is given.

    Args:
        value(str): a string to print
        way(int): the type of printing to perform, either 1 or 2

    Returns:
        None
    """

    value = str(value)
    value_list: list[str] = [i for i in value]
    value_count: int = len(value_list)

    if way == 1:
        for i in range(value_count):
            print("".join(value_list[0 : value_count - i]))

    elif way == 2:
        for i in range(value_count + 1):
            print("".join(value_list[0:i]))

    else:
        print("Please set the way: 1 for down, 2 for up")
