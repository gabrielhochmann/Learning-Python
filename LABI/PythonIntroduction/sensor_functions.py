# File: sensor_functions.py

def calculate_average(sensor_values):
    if not sensor_values:
        return 0.0
    return sum(sensor_values) / len(sensor_values)