from math import sqrt

def calculate_root(a, b, c, root_number):

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "The quadratic equation has no real roots."
    
    root_1 = (-b + sqrt(discriminant)) / (2 * a)
    root_2 = (-b - sqrt(discriminant)) / (2 * a)

    if root_number == 1:
        return root_1
    elif root_number == 2:
        return root_2
    else:
        return "Invalid Number, please input 1 or 2."


a = float(input("Input the coefficient of the quadratic term (a): "))
b = float(input("Input the coefficient of the liner term (b): "))
c = float(input("Input the constant term coefficient (c): "))
root = int(input("Which root do you want to calculate (1 or 2)?"))

result = calculate_root(a, b, c, root)
print(f"The X{root} is: {result:.2f}")
