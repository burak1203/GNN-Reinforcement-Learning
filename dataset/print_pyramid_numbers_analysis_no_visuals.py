def print_pyramid_numbers(rows: int) -> None:
    """
    Prints a pyramid of numbers pattern.

    Args:
        rows (int): The number of rows in the pyramid. Must be a positive integer.

    Returns:
        None

    Raises:
        rows must be integer

    Example:
        >>> print_pyramid_numbers(5)
        ====The Pyramid of Numbers Pattern====
            1
           2 2
          3 3 3
         4 4 4 4
        5 5 5 5 5
    """
    print("====The Pyramid of Numbers Pattern====")
    for i in range(1, rows + 1):
        for _ in range(rows, i, -1):
            print(end=" ")
        for _ in range(1, i + 1):
            print(i, end=" ")
        print()
