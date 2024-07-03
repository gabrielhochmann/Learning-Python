import math

# Area of a Circle

radius = float(input("Input the radius (r): "))
area_circle = math.pi * radius ** 2
print(f"The area of the circle is: {area_circle:.2f}")

# Quadratic formula

a = float(input("Input the Coefficient of the Quadratic term (a): "))
b = float(input("Input the Coefficient of the Liner term (b): "))
c = float(input("Input the Constant term coefficient (c): "))

discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots of the quadratic equation are: x1 = {x1}, x2 = {x2}")
else:
    print("The quadratic equation has no real roots.")

# Gravitational Force formula

m1 = float(input("Input the mass of the first object (m1) in kg: "))
m2 = float(input("Input the mass of the second object (m2) in kg: "))
radius = float(input("Input the radius (r) in meters: "))

G = 6.67 * 10 ** -11
F = G * ((m1 * m2) / (radius ** 2))

print(f"The gravitational force between the two objetct is: {F} Newtons")

# Volume of a Sphere formula

radius = float(input("Input the radius (r) of the sphere in meters: "))
V = 4/3 * math.pi * radius ** 3

print(f"The volume of the sphere with radius {radius} meters is: {V} cubic meters")

# Area of a triangle

b = float(input("Input the base length (b) of the triangle in meters: "))
h = float(input("Input the height (h) of the triangle in meters: "))
A = 1/2 * b * h

print(f"The area of the triangle with base {b} meters and height {h} meters is: {A} square meters")

# Exponential Function

xn = float(input("Input a number to cumpute the exponential function: "))
z = math.exp(xn)

print(f"The exponential of {xn} is: {z}")

# Power Function

y = float(input("Input the base number for the power function: "))
xn = float(input("Input the expoent for the power function: "))
z = y ** xn

print(f"The result of {y} raised to the power of {xn} is: {z}")

# Pythagorean Theorem

an = float(input("Input the length of side 'a' of the right triangle in meters: ")) 
bn = float(input("Input the length of side 'b' of the right triangle in meters: ")) 

c = math.sqrt(an ** 2 + bn ** 2)

print(f"The length of the hypotenuse 'c' of the right triangle is: {c} meters")

# Degrees to Radians Conversion

degrees = float(input("Input the angle in degrees: "))
rad = math.pi * degrees / 180

print(f"{degrees} degrees is equal to {rad} radians")

# Equation 1

xb = float(input("Input a number: ")) 
yb = float(input("Input a number: "))
zb = math.sqrt(xb ** 2 + yb ** 3) / abs(xb + yb)

print(f"The result is: {zb}")

# Equation 2

xa = float(input("Input a number: ")) 
zm = (1 + math.sin(xa)) / (1 + math.cos(xa))

print(f"The result is: {zm}")

# Equation 3

xk = float(input("Input a number: ")) 
zt = 1 + (1 / (xk)) + (1 / (xk ** 2)) + (1 / (xk ** 3)) + + (1 / (xk ** 4))

print(f"The result is: {zt}")

# Equation 4

xx = float(input("Input a number: ")) 
yy = float(input("Input a number: ")) 
zz = xx / yy - (xx + (xx/yy) ** 2) / (yy - (xx/yy) ** 2)

print(f"The result is: {zz}")

# Equation 5


xo = float(input("Input a number: ")) 
zo = math.sqrt(math.pi + math.sqrt(math.exp(3) + math.sqrt(4 + math.sqrt(xo))))

print(f"The result is: {zo}")