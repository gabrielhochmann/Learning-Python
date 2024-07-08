def get_kilometers_traveled():
    """
    Prompt the user to input the kilometers traveled.
    
    Returns:
    float: The number of kilometers traveled entered by the user.
    """
    return float(input("Input the kilometers traveled here: "))
    
def calculate_fuel_consumption(km):
   """
   Calculate the fuel consumption of the car based on the kilometers traveled.
   
   Parameters:
   km (float): The number of kilometers traveled.
   
   Returns:
   float: The fuel consumption in kWh.
   """ 
   return km * 6

def display_fuel_consumption(km, kwh):
    """
    Display the fuel consumption of the car.
    
    Parameters:
    km (float): The number of kilometers traveled.
    kwh (float): The fuel consumption in kWh.
    """
    print(f"The car consumed approximately {kwh:.2f} kWh over {km:.2f} kilometers")
    
def main():
    """
    Main function to execute the fuel consumption calculation.
    """
    
    km = get_kilometers_traveled()
    kwh = calculate_fuel_consumption(km)
    display_fuel_consumption(km, kwh)
    
if __name__ == "__main__":
    main()