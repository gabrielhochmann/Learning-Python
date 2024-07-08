from math import sqrt

def calculate_root(a, b, c, root_number):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None
    
    sqrt_discriminant = sqrt(discriminant)
    denominator = 2 * a
    
    if root_number == 1:
        return (-b + sqrt_discriminant) / denominator
    elif root_number == 2:
        return (-b - sqrt_discriminant) / denominator
    else:
        return None 

def main():
    a = float(input("Input the coefficient of the quadratic term (a): "))
    b = float(input("Input the coefficient of the liner term (b): "))
    c = float(input("Input the constant term coefficient (c): "))
    root_number = int(input("Which root do you want to calculate (1 or 2)?"))
    
    result = calculate_root(a, b, c, root_number)
    
    if result is None:
        print("The quadratic equation has no real roots or invalid input.")
    else:
       print(f"The X{root_number} is: {result:.2f}")

if __name__ == "__main__":
    main()
