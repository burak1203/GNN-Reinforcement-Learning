def print_simple_number(rows: int) -> None:
    """
    Prints a simple number pattern based on the given number of rows.

    Parameters:
        rows (int or float): The number of rows in the pattern. Must be a positive integer.

    Returns:
        None

    Raises:
        None

    Example:
        >>> print_simple_number(5)
        ====Printing Simple Number Pattern====
            1
           1 2
          1 2 3
         1 2 3 4
        1 2 3 4 5
    """

    print("====Printing Simple Number Pattern====")
    for i in range(1, rows + 1):
        print(*range(1, i + 1), sep=" ", end="\n")
