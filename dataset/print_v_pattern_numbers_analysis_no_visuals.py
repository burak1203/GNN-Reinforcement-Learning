def print_v_pattern_numbers(rows: int) -> None:
    """
        A function that prints the V Numbers Pattern based on the input number of rows.
    Parameters:
        rows (int): The number of rows for the V Numbers Pattern.
    Returns:
        None
    """

    if rows > 0:
        print("====The V Numbers Pattern====")
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end="")
            for k in range(1, 2 * (rows - i) + 1):
                print(k, end=" ")
            for l in range(i, 0, -1):
                print(l, end="")
            print()
    else:
        print("Take positive number")
