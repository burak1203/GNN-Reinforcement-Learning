def combination(input_list: list[int | float | str]) -> list[list[int | float | str]] | list[int | float | str]:
    """
    Generates all possible combinations of the elements in the input list.

    Args:
        input_list (list[int | float | str]): A list of integers, floats, or strings for which combinations are to be generated.

    Returns:
        list[list[int | float | str]] | list[int | float | str]: A list containing all possible combinations of the elements in the input list.
    """
    if len(input_list) == 1:
        return [[input_list[0]]]

    result: list[int | float | str] = []
    list_len: int = len(input_list)
    for i in range(list_len):
        for c in combination(input_list[:i] + input_list[i + 1:]):
            result.append([input_list[i]] + c)
    return result
