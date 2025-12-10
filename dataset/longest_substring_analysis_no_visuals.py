def longest_substring(string: str) -> int:
    """
    A function that finds the length of the longest substring without repeating characters.

    Args:
        string (str): The input string for which the longest substring length is to be found.

    Returns:
        int: The length of the longest substring without repeating characters.
    
    Example:
        >>> longest_substring("hello world")
        6
    """
    start: int = 0
    max_length: int = 0
    char_map: dict[str, int] = {}
    for i, char in enumerate(string):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length
