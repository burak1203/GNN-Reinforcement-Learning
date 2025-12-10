def mean(*numbers: int | float) -> None:
    """
    Calculates the mean of the input numbers.

    Parameters:
        *numbers: int or float - variable number of integer or float numbers

    Returns:
        None
    """


    total: int | float = sum(numbers)
    total_count: int = len(numbers)
    result: float = total / total_count
    print(f"Mean: {result}")
