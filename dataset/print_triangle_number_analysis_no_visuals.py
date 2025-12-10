def print_triangle_number(rows: int) -> None:
    """
    Prints a triangle number pattern based on the given number of rows.

    Args:
        rows (int): The number of rows in the triangle pattern.

    Returns:
        None: This function does not return anything.

    Raises:
        None: This function does not raise any exceptions.

    Examples:
        >>> print_triangle_number(5)
        ====The Triangle Numbers Pattern====
            1
           1 2
          1 2 3
         1 2 3 4
        1 2 3 4 5

    >>> print_triangle_number(-5)
        take positive number

    >>> print_triangle_number(5.5)
        take positive integer number

    >>> print_triangle_number("5")
        take positive integer number
    """

    print("====The Triangle Numbers Pattern====")
    for i in range(1, rows + 1):
        for _ in range(rows, i, -1):
            print(end=" ")
        for k in range(1, i + 1):
            print(k, end=" ")
        print()
