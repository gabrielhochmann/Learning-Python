# File: sensor_main_program.py 
from sensor_functions import calculate_average

def handle_sensor_data(sensor_count=3):
    sensor_values = []
    for i in range(sensor_count):
        sensor_values.append(float(input("Input the sensor reading {i+1}: ")))
    
    average = calculate_average(sensor_values)

    print(f"The average sensor reading is: {average:.2f}")

if __name__ == "__main__":
    handle_sensor_data(sensor_count=3)

