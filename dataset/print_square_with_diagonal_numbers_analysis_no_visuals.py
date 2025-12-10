def print_square_with_diagonal_numbers(rows: int) -> None:
    """
    Prints a square pattern with diagonal numbers and remaining zeros.

    Args:
    rows (int): The number of rows in the square pattern.

    Returns:
        None

    Raises:
        None

    Example:
        >>> print_square_with_diagonal_numbers(5)
        ====The Square With Diagonal Numbers and Remaining 0 Pattern====
        0 1 0 0 0
        0 2 0 0 0
        0 3 0 0 0
        0 4 0 0 0
        0 5 0 0 0

    Note:
        - If the input `rows` is not an integer or is less than or equal to 0,
            it prints "take positive number".
        - If the input `rows` is a float, it prints "take positive integer number".
    """
    for i in range(1, rows + 1):
        for _ in range(1, i):
            print(0, end=" ")
        print(i, end=" ")
        for _ in range(i, rows):
            print(0, end=" ")
        print()
