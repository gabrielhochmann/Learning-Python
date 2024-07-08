import math

# Area of a Circle

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    return math.pi * radius ** 2

def solve_quadratic(a, b, c):
    """
    Solve a quadratic equation ax^2 + bx + c = 0
    
    Parameters:
    a, b, c (float): Coefficients of the quadratic equation.
    
    Returns:
    tuple: Roots of the quadratic equation or a message if no real roots exist.
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    else:
        return "The quadratic equation has no real roots."


def calculate_gravitational_force(m1, m2, radius):
    """
    Calculate the gravitational force between two objects.
    
    Parameters:
    m1, m2 (float): Masses of the objects.
    radius (float): Distance between the objects.
    
    Returns:
    float: The gravitational force between the objects.
    """
    G = 6.67 * 10 ** -11
    return G * ((m1 * m2) / (radius ** 2))


def calculate_sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.
    
    Parameters:
    radius (float): The radius of the sphere.
    
    Returns:
    float: The volume of the sphere.
    """
    return 4/3 * math.pi * radius ** 3

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.
    
    Parameters: base, height (float): Base and height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return 1/2 * base * height 

def calculate_exponential(x):
    """
    Calculate the exponential of a number.
    
    Parameters:
    x (float): The number to calculate the exponential of.
    
    Returns:
    float: The exponential of the number.
    """
    return math.exp(x)

def calculate_power(base, exponent):
    """
    Calculate the power of a number given a base and an exponent.
    
    Parameters:
    base, exponent (float): The base and exponent.
    
    Returns:
    float: The result of base raised to the power of exponent.
    """
    return base ** exponent

def calculate_hypotenuse(a, b):
    """
    Calculate the hypotenuse of a right triangle given its two sides.
    
    Parameters:
    a, b (float): The lengths of the two sides.
    
    Returns:
    float: The length of the hypotenuse.
    """
    return math.sqrt(a ** 2 + b ** 2)

def degrees_to_radians(degrees):
    """
    Convert an angle from degrees to radians.
    
    Parameters:
    degrees (float): The angle in degrees.
    
    Returns:
    float: The angle in radians.
    """
    return math.pi * degrees / 180

def equation1(x, y):
    """
    Calculate the result of a specific equation involving two numbers.
    
    Parameters:
    x, y (float): The input numbers.
    
    Returns:
    float: The result of the equation.
    """
    return math.sqrt(x ** 2 + y ** 3) / abs(x + y)

def equation2(x):
    """
    Calculate the result of a specific trigonometric equation.
    
    Parameters:
    x (float): The input number.
    
    Returns:
    float: The result of the equation.
    """
    return (1 + math.sin(x)) / (1 + math.cos(x))

def equation3(x):
    """
    Calculate the result of a specific polynomial equation.
    
    Parameters:
    x (float): The input number.
    
    Returns:
    float: The result of the equation.
    """
    return 1 + (1 / (x)) + (1 / (x ** 2)) + (1 / (x ** 3)) + (1 / (x ** 4))

def equation4(x, y):
    """
    Calculate the result of a specific algebraic equation.
    
    Parameters:
    x, y (float): The input numbers.
    
    Returns:
    float: The result of the equation.
    """
    return x / y - (x + (x / y) ** 2) / (y - (x/y) ** 2)

def equation5(x):
    """
    Calculate the result of a specific nested square root equation.
    
    Parameters:
    x (float): The input number.
    
    Returns:
    float: The result of the equation.
    """
    return math.sqrt(math.pi + math.sqrt(math.exp(3) + math.sqrt(4 + math.sqrt(x))))

def main():
    # Area of a Circle
    radius = float(input("Input the radius (r): "))
    area_circle = calculate_circle_area(radius)
    print(f"The area of the circle is: {area_circle:.2f}")
    
    # Quadratic Formula
    a = float(input("Input the Coefficient of the Quadratic term (a): "))
    b = float(input("Input the Coefficient of the Liner term (b): "))
    c = float(input("Input the Constant term coefficient (c): "))
    roots = solve_quadratic(a, b, c)
    if isinstance(roots, tuple):
        x1, x2 = roots
        print(f"The roots of the quadratic equation are: x1 = {x1}, x2 = {x2}")
    else:
        print(roots)
        
    # Gravitational Force
    m1 = float(input("Input the mass of the first object (m1) in kg: "))
    m2 = float(input("Input the mass of the second object (m2) in kg: "))
    radius = float(input("Input the radius (r) in meters: "))
    force = calculate_gravitational_force(m1, m2, radius)
    print(f"The gravitational force between the two objetct is: {force} Newtons")
    
    # Volume of a Sphere
    radius = float(input("Input the radius (r) of the sphere in meters: "))
    volume_sphere = calculate_sphere_volume(radius)
    print(f"The volume of the sphere with radius {radius} meters is: {volume_sphere: .2f} cubic meters")

    # Area of a Triangle
    base = float(input("Input the base length (b) of the triangle in meters: "))
    height = float(input("Input the height (h) of the triangle in meters: "))
    area_triangle = calculate_triangle_area(base, height)
    print(f"The area of the triangle with base {base} meters and height {height} meters is: {area_triangle: .2f} square meters")

    # Exponential Function
    x = float(input("Input a number to cumpute the exponential function: "))
    exp_result = calculate_exponential(x)
    print(f"The exponential of {x} is: {exp_result}")

    # Power Function
    base = float(input("Input the base number for the power function: "))
    exponent = float(input("Input the expoent for the power function: "))
    power_result = calculate_power(base, exponent)
    print(f"The result of {base} raised to the power of {exponent} is: {power_result}")
    
    # Pythagorean Theorem
    a = float(input("Input the length of side 'a' of the right triangle in meters: ")) 
    b = float(input("Input the length of side 'b' of the right triangle in meters: "))
    hypotenuse = calculate_hypotenuse(a, b) 
    print(f"The length of the hypotenuse 'c' of the right triangle is: {hypotenuse} meters")

    # Degrees to Radians Conversion
    degrees = float(input("Input the angle in degrees: "))
    radians = degrees_to_radians(degrees)
    print(f"{degrees} degrees is equal to {radians} radians")
    
    # Equation 1
    x = float(input("Input a number (x) for equation 1: ")) 
    y = float(input("Input a number (y) for equation 1: ")) 
    result1 = equation1(x, y)
    print(f"The result of equation 1 is: {result1}")
    
    # Equation 2
    
    x = float(input("Input a number (x) for equation 2: ")) 
    result2 = equation2(x)
    print(f"The result of equation 2 is: {result2}")
    
    # Equation 3
    x = float(input("Input a number (x) for equation 3: ")) 
    result3 = equation3(x)
    print(f"The result of equation 3 is: {result3}")
    
    # Equation 4
    x = float(input("Input a number (x) for equation 4: ")) 
    y = float(input("Input a number (y) for equation 4: ")) 
    result4 = equation4(x, y)
    print(f"The result of equation 4 is: {result4}")
    
    # Equation 5
    x = float(input("Input a number (x) for equation 5: ")) 
    result5 = equation5(x)
    print(f"The result of equation 5 is: {result5}")
    
if __name__ == "__main__":
    main()