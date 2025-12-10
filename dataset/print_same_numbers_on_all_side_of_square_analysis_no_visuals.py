def print_same_numbers_on_all_side_of_square(rows: int) -> None:
    """
    Prints the same numbers on all sides of a square pattern.

    Parameters:
        rows (int): The number of rows in the square pattern.

    Returns:
        None

    Raises:
        None

    Examples:
        >>> print_same_numbers_on_all_side_of_square(5)
        ====Print Same Numbers on all Sides of a Square Pattern====
        5 4 4 4 5
        4 3 3 3 4
        4 3 3 3 4
        4 3 3 3 4
        5 4 4 4 5
        5 4 4 4 5
    """
    print("====Print Same Numbers on all Sides of a Square Pattern====")

    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            if i < j:
                print(rows - i + 1, end=" ")
            else:
                print(rows - j + 1, end=" ")
        for k in range(rows - 1, 0, -1):
            if i < k:
                print(rows - i + 1, end=" ")
            else:
                print(rows - k + 1, end=" ")
        print()

    for i in range(rows - 1, 0, -1):
        for j in range(1, rows + 1):
            if i < j:
                print(rows - i + 1, end=" ")
            else:
                print(rows - j + 1, end=" ")
        for k in range(rows - 1, 0, -1):
            if i < k:
                print(rows - i + 1, end=" ")
            else:
                print(rows - k + 1, end=" ")
        print()
