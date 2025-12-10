def print_square_pattern_numbers(rows: int) -> None:
    """
    Prints a square pattern of left shift numbers based on the given number of rows.

    Parameters:
        rows (int): The number of rows in the square pattern.
        Must be a positive integer less than 1000.

    Returns:
        None

    Raises:
        None

    Example:
        >>> print_square_pattern_numbers(5)
        1 2 3 4 5
        2 3 4 5 1
        3 4 5 1 2
        4 5 1 2 3
        5 1 2 3 4
    """

    print("====The Square Pattern of Left Shift Numbers====")

    for i in range(1, rows + 1):
        for j in range(i, rows + 1):
            print(j, end=" ")
        for k in range(1, i):
            print(k, end=" ")
        print()
    print()
