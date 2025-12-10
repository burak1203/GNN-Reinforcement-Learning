def longest_palindrome(string: str) -> str:
    """
    Finds the longest palindrome substring in the given input string.

    Parameters:
        string (str): The input string to search for palindrome substrings.

    Returns:
        str: The longest palindrome substring found in the input string.
    
    Example:
        >>> longest_palindrome("hello world")
        'll'
    """
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    max_len: int = 0
    start: int = 0

    for i in range(len(string)):
        for j in range(i, len(string)):
            if is_palindrome(string[i:j+1]) and len(string[i:j+1]) > max_len:
                start = i
                max_len = len(string[i:j+1])

    return string[start:start+max_len]
