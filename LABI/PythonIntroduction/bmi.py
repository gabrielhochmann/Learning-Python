# Body Mass Index (BMI)

def calculate_bmi(w, h):

    if h <= 0 or w <= 0:  
        raise ValueError("Error: Height and weight must be positive numbers.")
    
    BMI = w / (h ** 2)
    return BMI

def main(): 
    try:
        age = int(input("Input your age: "))
        weight = float(input("Input your weight in kg: "))
        height = float(input("Input your height in meters: "))

        BMI = calculate_bmi(weight, height)
        print(f"Your BMI is {BMI:.2f}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values for age, weight, and height.")

if __name__ == "__main__":
    main()