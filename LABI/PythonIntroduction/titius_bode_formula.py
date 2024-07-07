def titius_bode_formula(planet_id):
    if planet_id == 1:
        return 0.4
    else:
        return round(0.4 + 0.3 * 2 ** (planet_id - 2), 2)

def main():
    planet_id = int(input("Enter the planet ID: "))
    print(f"The Titius-Bode distance for planet ID {planet_id} is: {titius_bode_formula(planet_id)}")

if __name__ == "__main__":
    main()