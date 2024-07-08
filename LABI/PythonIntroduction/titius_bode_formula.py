def titius_bode_formula(planet_id):
    """
    Calculates the Titius-Bode distance formula for a given planet ID.
    
    Args:
    - planet_id (int): ID of the planet (1 for Mercury, 2 for Venus, etc.).
    
    Returns:
    - float: Calculated Titius-Bode distance.
    """
    if planet_id == 1:
        return 0.4
    else:
        return round(0.4 + 0.3 * 2 ** (planet_id - 2), 2)

def main():
    """
    Main function to interactively get planet ID from user and print the calculated Titius-Bode distance.
    """
    
    try:
        planet_id = int(input("Enter the planet ID: "))
    except ValueError:
        print("Error: Please enter a valid integer for planet ID.")
    
    if planet_id <= 0:
        print("Error: Planet ID should be greater than zero.")
        return
    
    titius_bode_distance = titius_bode_formula(planet_id)
    print(f"The Titius-Bode distance for planet ID {planet_id} is: {titius_bode_distance}")

if __name__ == "__main__":
    main()