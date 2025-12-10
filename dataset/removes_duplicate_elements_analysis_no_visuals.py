def removes_duplicate_elements(value_list: list[int | str | float]) -> list[int | str | float]:
    """
    Removes duplicate elements from a list and prints a message for each duplicate element.

    Args:
        value_list (list[int | str | float]): The list from which duplicate elements will be removed.

    Returns:
        list[int | str | float]: The list with duplicate elements removed.

    Example:
        >>> removes_duplicate_elements([1, 1, 2, 2, 3, 4])
        1 it was deleted because it was on the list.
        2 it was deleted because it was on the list.
        [1, 2, 3, 4]
    """
    new_list: set[str | int | float] = set()
    if value_list:
        for value in value_list:
            if value_list.count(value) > 1:
                print(f"{value} it was deleted because it was on the list.")
            new_list.add(value)

    else:
        return value_list

    return list(new_list)
