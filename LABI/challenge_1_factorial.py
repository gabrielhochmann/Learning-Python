import math

def factorial_iteractive(n):
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

def factorial_recursive(n):
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
        return n * factorial_recursive(n - 1)
    
def factorial_tail_recursive(n, acc = 1):
    """
    Calculate the factorial of a given number using tail recursion.
    
    Args:
    n (int): The number for which factorial is to be calculated.
    acc (int): The accumulator that holds the result of the factorial calculation.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return acc
    else:
        return factorial_tail_recursive(n - 1, n * acc)
    
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
    Main function to interactively choose between iterative, recursive, and tail recursive factorial calculation.
    """
    x = get_user_input()
    
    print("Choose method to calculate factorial:")
    print("1. Iterative")
    print("2. Recursive")
    print("3. Tail Recursive")
    
    choice = input("Enter your choice (1, 2 or 3): ")
    
    if choice == '1':
        result = factorial_iteractive(x)
        method = "iteratively"
    elif choice == '2':
        result = factorial_recursive(x)
        method = "recursively"
    elif choice == '3':
        result = factorial_tail_recursive(x, 1)
        method = "tail recursively"
    else:
        print("Error: Invalid choice. Please enter 1, 2 or 3.")
        return
    
    print(f"Factorial of {x} calculated {method} is: {result}")

#Summary and differences between factorial calculation methods

"""
Differences between iterative and recursive approaches to factorial calculation:

Interactive factorial:
- The maximum calculable factorial is 1558.
-- This is because the iterative method uses the math.prod() function, which can handle larger numbers than the recursive methods, as it doesn't rely on the call stack for recursion, thus has lower memory costs.

Recursive factorial:
The maximum calculable factorial is 997.
-- This is because the recursive method uses the call stack for recursion, which has a limited size. Thus, it can't handle larger numbers than the iterative method, as the maximum calculable is limited by the maximum recursion depth of the programing environment.

Tail Recursive factorial:
The maximum calculable factorial is 997.
-- The maximum calculable factorial is also limited by the recursion depth if the language/runtime doesn't support tail call optimization. In this case, the maximum calculable factorial is the same as the recursive method.

Summary:
The iterative method is the most efficient in terms of memory usage and performance, as it doesn't rely on the call stack for recursion. The recursive and tail recursive methods are limited by the maximum recursion depth of the programming environment, which can be a limiting factor for large factorials.
It was expected that the tail recursive method would be more efficient than the recursive method, but in this case, the maximum calculable factorial is the same for both methods, indicating that the language/runtime doesn't support tail call optimization.

"""

if __name__ == "__main__":
    main()
