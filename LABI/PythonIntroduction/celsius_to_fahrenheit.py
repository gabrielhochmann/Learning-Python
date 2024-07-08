# This program converts a temperature given in degrees Celsius to Fahrenheit. 

def celsius_to_fahrenheit (celsius_degree):
    return celsius_degree * 1.8 + 32

def main():
    # Prompt the user to input the temperature in Celsius
    Ce = float(input("Input the degrees Celsius (Ce) "))
    # Display the result in Fahrenheit
    print(f"{Ce}° Celsius in Fahrenheit is {celsius_to_fahrenheit(Ce)}°")

if __name__ == "__main__":
    main()