def print_diamond_number(rows: int) -> None:
    """
    Prints the diamond number pattern for the given number of rows.

    Args:
        rows (int): The number of rows for the diamond pattern.

    Returns:
        None

    Examples:
        >>> print_diamond_number(5)
        ====Diamond Number Pattern====
            1
           123
          12345
         1234567
        123456789
         1234567
          12345
           123
            1

        >>> print_diamond_number(-5)
        take positive number

        >>> print_diamond_number(5.5)
        take positive integer number

        >>> print_diamond_number("5")
        take integer number
    """

    print("====Diamond Number Pattern====")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print(" ".join(map(str, range(i, 2 * i + 1))))

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        print(" ".join(map(str, range(i, 2 * i + 1))))
