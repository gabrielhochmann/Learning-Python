import datetime

def get_foundation_year():
    """
    Prompt the user to input the foundation year of the enterprise.
    
    Returns:
    int: The foundation year entered by the user.
    """
    return int(input("Input the foundation year: "))
    
def calculate_age (foundation_year):
    """
    Calculate the current age of the enterprise based on the foundation year.
    
    Parameters:
    foundation_year (int): The year that the enterprise was founded.
    
    Returns:
    int: The current age of the enterprise.
    """
    current_year = datetime.datetime.now().year
    return current_year - foundation_year

def display_age(age):
    """
    Display the current age of the enterprise.
    
    Parameters:
    age (int): The current age of the enterprise.
    """
    print(f"Actual age of the Enterprise is: {age}")

def main():
    """
    Main function to execute the age calculation.
    """
    foundation_year = get_foundation_year()
    age = calculate_age(foundation_year)
    display_age(age)

if __name__ == "__main__":
    main()