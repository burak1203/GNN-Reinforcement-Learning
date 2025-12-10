def print_consecutive_rows_numbers_in_right_triangle(rows: int) -> None:
    """
    Prints consecutive rows of numbers in a right triangle.

    Args:
        rows (int): The number of rows in the right triangle.
    """
    for i in range(1, rows + 1):
        val: int = i
        for j in range(1, i + 1):
            print(val, end=" ")
            val = val + rows - j
        print()
