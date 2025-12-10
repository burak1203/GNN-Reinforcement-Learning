def print_sandglass_number(rows: int) -> None:
    """
    Prints the sandglass number pattern based on the given number of rows.

    Parameters:
        rows (int): The number of rows in the sandglass pattern.

    Returns:
        None

    Raises:
        None

    Example:
        >>> print_simple_number(5)
        ====Printing Simple Number Pattern====
        1 2 3 4 5
         2 3 4 5
          3 4 5
           4 5
            5
           4 5
          3 4 5
         2 3 4 5
        1 2 3 4 5
    """

    print("====Sandglass Number Pattern====")

    # first half
    for i in range(1, rows + 1):
        print(" " * (i), end="")
        print(" ".join(map(str, range(i, rows + 1))))

    # second half
    for i in range(rows - 1, 0, -1):
        print(" " * (i), end="")
        print(" ".join(map(str, range(i, rows + 1))))
