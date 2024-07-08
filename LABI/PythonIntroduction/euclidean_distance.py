from math import sqrt

def calculate_distance (x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).
    
    Parameters:
    x1, y1 (float): Coordinates of the first point.
    x2, y2 (float): Coordinates of the second point.
    
    Returns:
    float: The distance between the two points.
    """
    
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_coordinates(point_name):
    """
    Prompt the user to input the coordinates of a point.
    
    Parameters:
    point_name (str): The name of the point to prompt the user.
    
    Returns:
    tuple: a tuple containing the x and y coordinates as floats.
    
    """
    x = float(input(f"Input the {point_name} x coordinate: "))
    y = float(input(f"Input the {point_name} y coordinate: "))
    return x, y

def main():
    """
    Main function to execute the distance calculation.
    """
    
    # Get coordinates of the first point
    x1, y1 = get_coordinates("first point (x1, y1)")
    
    # Get coordinates of the second point
    x2, y2 = get_coordinates("second point (x2, y2)")
    
    # Calculate the distance
    distance = calculate_distance(x1, y1, x2, y2)

    print(f"The distance beetwen ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f})")

if __name__ == "__main__":
    main()