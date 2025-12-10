def check_leap_year(year: int) -> None:
    """
    Check if a given year is a leap year.

    Parameters:
        year (int): The year to be checked.

    Returns:
        None
    """
    isleap: bool = any([year % 400 == 0, year % 4 == 0 and year % 100 != 0])

    if isleap:
        print(year, "is a leap year")
    else:
        print(year, "is not")
