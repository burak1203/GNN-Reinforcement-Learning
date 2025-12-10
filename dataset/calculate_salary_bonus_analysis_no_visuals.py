def calculate_salary_bonus(salary: float, children_count: int) -> float:
    """
    Calculates the bonus amount for a given salary and number of children.

    Args:
        salary (float): The salary amount.
        children_count (int): The number of children.

    Returns:
        float: The bonus amount.
    """
    bonus: float = 0

    if children_count >= 3:
        bonus = salary * (10 / 100)
    elif children_count == 2:
        bonus = salary * (5 / 100)
    elif children_count == 1:
        bonus = salary * (3 / 100)
    else:
        bonus = salary * (1 / 100)

    return bonus
