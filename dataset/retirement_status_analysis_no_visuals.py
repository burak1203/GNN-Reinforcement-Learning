def retirement_status(age: int, number_of_prime_days: int) -> None:
    """
    Checks the retirement status of a person based on their age and number of prime days.

    Args:
        age (int): The age of the person.
        number_of_prime_days (int): The number of prime days the person has.

    Returns:
        None
    """

    if age > 65 and number_of_prime_days >= 7000:
        print("You can retire.")

    elif age > 65 and number_of_prime_days < 7000:
        print(f"You must complete {7000 - number_of_prime_days} premium day.")

    elif age <= 65 and number_of_prime_days >= 7000:
        print(
            f"Your insurance premium is sufficient, but you must work {66 - age} more years to retire."
        )

    else:
        print("You cannot retire yet, your premiums and age are not appropriate.")
