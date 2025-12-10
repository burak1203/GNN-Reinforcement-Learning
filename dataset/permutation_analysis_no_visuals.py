def permutation(sequence: list[int | str | float]) -> list[list[int | str | float]]:
    """
    Generates all possible permutations of a given sequence.

    Args:
        sequence (list[int | str | float]): The input sequence for which permutations are to be generated.

    Returns:
        list[list[int | str | float]]: A list of lists, where each inner list represents a permutation of the input sequence.

    Raises:
        None

    Examples:
        >>> permutation([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        >>> permutation([1])
        [[1]]

        >>> permutation([])
        [[]]

        >>> permutation(1)
        Please enter a list; for example: [1]
    """

    if len(sequence) == 1:
        return [sequence]

    result: list[list[int | str | float]] = []
    for i in range(len(sequence)):
        for perm in permutation(sequence[:i] + sequence[i + 1 :]):
            result.append([sequence[i]] + perm)

    return result