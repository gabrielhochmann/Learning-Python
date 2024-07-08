def rectangle_measurements(L1, L2):
    """
    Calculate the area and perimeter of a rectangle given its sides L1 and L2.
    
    Args:
    L1 (float): Length of the rectangle in centimeters.
    L2 (float): Width of the rectangle in centimeters.
    
    Returns:
    tuple: A tuple containing the area and perimeter of the rectangle.
    """
    area = L1 * L2
    perimeter = 2 * (L1 + L2)
    return (area, perimeter)

def main():
    # Prompt the user to enter the dimensions of the rectangle
    L1 = float(input("Enter the length of the rectangle (L1 in cm): "))
    L2 = float(input("Enter the length of the rectangle (L1 in cm): "))
    
    # Calculate the area and perimeter using the function
    area, perimeter = rectangle_measurements(L1, L2)
    
    # Print the results
    print(f"\nArea of the rectangle with L1 = {L1} cm and L2 = {L2} cm: {area} cm²")
    print(f"Perimeter of the rectangle with L1 = {L1} cm and L2 = {L2} cm: {perimeter} cm")

if __name__ == "__main__":
    main()