# File: sensor_main_program.py 
from sensor_functions import calculate_average

def handle_sensor_data(sensor_count=3):
    """
    Collects sensor readings from the user and calculates the average.
    
    Args:
    - sensor_count (int): Number of sensor readings to collect. Default is 3.
    
    Returns:
    - None
    """
    sensor_values = []
    for i in range(sensor_count):
        try:
            sensor_reading = float(input(f"Input the sensor reading {i+1}: "))
        except ValueError:
            print("Error: Please enter a valid numeric value.")
            return # Exit function if invalid input is detected
        
        sensor_values.append(sensor_reading)
    
    average = calculate_average(sensor_values)

    print(f"The average sensor reading is: {average:.2f}")

if __name__ == "__main__":
    print("Enter sensor readings to calculate average:")
    handle_sensor_data(sensor_count=3)

