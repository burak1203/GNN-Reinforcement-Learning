def fibonacci(nterms: int) -> None:
    """
    Generates a Fibonacci sequence up to the specified number of terms.

    Parameters:
        nterms (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
        None

    Raises:
        None

    Example:
        >>> fibonacci(5)
        Fibonacci sequence:
        0
        1
        1
        2
        3
    """
    
    
    # first two terms
    n1, n2 = 0, 1
    count: int = 0

    if nterms >= 1:
        # generate fibonacci sequence
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth: int = n1 + n2

            # update values
            n1 = n2
            n2 = nth
            count += 1
    else:
        print("Please enter a positive integer")
