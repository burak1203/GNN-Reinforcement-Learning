def body_mass_index(weight: float, height: float) -> None:
    """
    Calculates the body mass index (BMI) based on the given weight and height.
    Args:
        weight (float): The weight of the person in kilograms.
        height (float): The height of the person in centimeters.
    Returns:
        None
    """
    mass_index: float = (weight / (height**2)) * 10_000
    if mass_index < 18.49:
        print("Underweight")
    elif mass_index > 18.5 and mass_index < 24.99:
        print("Normal")
    elif mass_index > 25 and mass_index < 29.99:
        print("Overweight")
    else:
        print("Obese")