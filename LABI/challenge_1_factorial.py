# First Challenge - Factorial

# Calculating the factorial of a given number interactively

def factorial(n):
    if n < 0:
        return "Error: The given number must be a positive number"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

n = int(input("Input a positive number: "))
print(f"Factorial of {n} is: {factorial(n)}")

# Calculating the factorial of a given number recursively

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    elif n == 0:
        return 1
    else:
        return -1
    
def main():
    x = int(input("Input a positive number: "))
    result = factorial(x)
    print(f"Factorial of {x} is: {result}")

if __name__ == "__main__":
    main()

"""
Differences between interactively and recursively:

Interactive factorial:
The maximum calculable factorial is 1558.

Recursive factorial:
The maximum calculable factorial is 997.

Therefore, the iterative method in this case is more efficient, as it has lower memory costs (since it doesn't use the call stack) compared to the recursive approach.
"""