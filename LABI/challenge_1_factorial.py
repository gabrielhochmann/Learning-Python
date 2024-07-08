import math

def factorial_iteractively(n):
    """
    Calculate the factorial of a given number iteratively.
    
    Args:
    n (int): The number for which factorial is to be calculated.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return math.prod(range(1, n+1))

def factorial_recursively(n):
    """
    Calculate the factorial of a given number recursively.
    
    Args:
    n (int): The number for which factorial is to be calculated.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursively(n-1)
    
def get_user_input():
    """
    Get a non-negative integer input from the user.
    
    Returns:
    int: The non-negative integer input.
    """
    while True: # to get a valid input
        try:
            x = int(input("Input a non-negative integer: "))
            if x >= 0:
                return x
            else:
                print("Error: Please enter a non-negative integer.")
        except ValueError:
            print("Error: Please enter a valid integer.")
        
def main():
    """
    Main function to interactively choose between iterative and recursive factorial calculation.
    """
    x = get_user_input()
    
    print("Choose method to calculate factorial:")
    print("1. Iterative")
    print("2. Recursive")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        result = factorial_iteractively(x)
        method = "iteratively"
    elif choice == '2':
        result = factorial_recursively(x)
        method = "recursively"
    else:
        print("Error: Invalid choice. Please enter 1 or 2.")
        return
    
    print(f"Factorial of {x} ({method}) is: {result}")
    
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