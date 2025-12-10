def print_inverted_right_triangle_of_decreasing_order_numbers(rows: int) -> None:
    """Print an inverted right triangle of decreasing order numbers.

    Args:
        rows (int): The number of rows in the triangle.
    
    Returns:
        None
    """

    print("==Inverted Right Triangle of Numbers in Decreasing Order Pattern==")
    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
