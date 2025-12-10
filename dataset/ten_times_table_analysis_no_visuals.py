def ten_times_table(number: int | float) -> None:
    """
    Prints the multiplication table for a given number.

    Parameters:
        number (int | float): The number for which the multiplication table is to be printed.

    Returns:
        None

    Raises:
        None
    """
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i} ")
