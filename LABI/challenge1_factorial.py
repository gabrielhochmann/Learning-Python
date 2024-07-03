# First Challenge - Factorial

# Calculating the factorial of a given number interactively

n = int(input("Input a number (greatest than 0): "))


if n < 0:
    print("Error: The given number must be a positive number")
elif n == 0:
    print("Factorial is: 1")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial is: {result}")

# Calculating the factorial of a given number recursively

"""
Differences between interactively and recursively:

"""