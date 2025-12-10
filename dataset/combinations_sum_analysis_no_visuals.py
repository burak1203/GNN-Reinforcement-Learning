def combinations_sum(input_list: list[int]) -> int:
    """
    Calculate the sum of all possible combinations of elements in the input list.

    Args:
        input_list (list[int]): The list of integers to calculate combinations from.

    Returns:
        int: The sum of all possible combinations of elements in the input list.
    """
    import itertools

    combinations: list[int] = []
    for r in range(0, len(input_list) + 1):
        combinations += list(itertools.combinations(input_list, r))
    return sum(map(sum, combinations))
