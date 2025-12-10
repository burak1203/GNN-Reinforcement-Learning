def print_floyd_triangle(rows: int) -> None:
    """
    Prints a Floyd's triangle with the given number of rows.

    Parameters:
        rows (int): The number of rows in the triangle. Must be a positive integer.

    Returns:
        None

    Raises:
        None

    Example:
        >>> print_floyd_triangle(5)
        Floyds Triangle
        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
    """
    print("Floyds Triangle")
    number: int = 1
    for i in range(1, rows + 1):
        for _ in range(1, i + 1):
            print(number, end=" ")
            number = number + 1
        print()
