def print_left_arrow_numbers_pattern(rows: int) -> None:
    """
    Prints the left arrow numbers pattern based on the given number of rows.

    Parameters:
        rows (int): The number of rows in the pattern.

    Returns:
        None

    Raises:
        None

    Examples:
        >>> print_left_arrow_numbers_pattern(5)
        5 4 3 2 1
        4 3 2 1
        3 2 1
        2 1
        1
        2 1
        3 2 1
        4 3 2 1
        5 4 3 2 1

        >>> print_left_arrow_numbers_pattern(-1)
        take positive number

        >>> print_left_arrow_numbers_pattern(1.0)
        take positive integer number
    """

    print("====The Left Arrow Numbers Pattern====")

    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    for i in range(2, rows + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
