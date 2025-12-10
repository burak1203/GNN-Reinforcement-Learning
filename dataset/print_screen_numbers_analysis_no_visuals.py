def print_screen_numbers(number: int) -> None:
    """
    Prints the numbers from 1 to the given number.

    Parameters:
        number (int): The number up to which the numbers will be printed.

    Returns:
        None
    """
    
    if number <= 0:
        print("Enter positive number")
        return

    count: int = 1
    while True:
        print(count)
        count += 1
        if count > number:
            break
