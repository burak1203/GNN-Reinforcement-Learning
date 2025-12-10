def print_right_triangle_of_numbers_in_sine_wave(rows: int) -> None:
    """
    Prints a right triangle of numbers in a sine wave pattern.

    Args:
        rows (int): The number of rows in the triangle. Must be a positive integer.

    Returns:
        None

    Raises:
        TypeError: If the input is not an integer or is not greater than 0.

    Example:
        >>> print_right_triangle_of_numbers_in_sine_wave(5)
        1
        2 9
        3 8 10
        4 7 11 14
        5 6 12 13 15
    """

    print("====The Right Triangle of Numbers in Sine Wave Pattern====")
    for i in range(1, rows + 1):
        print(i, end=" ")
        num = i
        for j in range(1, i):
            if j % 2 != 0:
                print((num + ((2 * (rows - i + 1)) - 1)), end=" ")
                num = num + (2 * (rows - i + 1) - 1)
            else:
                print(num + 2 * (i - j), end=" ")
                num = num + 2 * (i - j)
        print()
