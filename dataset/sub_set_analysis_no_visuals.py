def sub_set(input_list: list[int | float | str]) -> list[list[int | float | str]]:
    """
    Generates all possible subsets of the input list.

    Args:
    input_list (list[int | float | str]): The list from which to generate subsets.

    Returns:
    list[list[int | float | str]]: A list of all possible subsets of the input list.
    """

    subsets: list[list[int | float | str]] = []
    for i in range(2 ** len(input_list)):
        subset: list[int | float | str] = []
        for j in range(len(input_list)):
            if i & (1 << j):
                subset.append(input_list[j])
        subsets.append(subset)
    return subsets
