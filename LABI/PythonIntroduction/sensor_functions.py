# File: sensor_functions.py

def calculate_average(sensor_values):
    """
    Calculate the average of sensor values.
    
    Args:
    - sensor_values (list of float): List of sensor readings.
    
    Returns:
    - float: Average value of sensor readings. Returns 0.0 if sensor_values is empty.
    """
    if not sensor_values:
        return 0.0
    return sum(sensor_values) / len(sensor_values)