import matplotlib.pyplot as plt

def f(t, y):
    """
    Define the differential equation dy/dt = -2y
    
    Parameters:
    t(float): Independent variable (time).
    y(float): Dependent variable.
    
    Returns:
    Float: The result of the differential equation.
    """
    return -2 * y

def euler_method(f, t0, y0, h, n):
    """
    Implements the Euler method for solving ordinary differential equations.
    
    Parameters:
    f (function): The function defining the differential equation.
    t0 (float): Initial value of the independent variable.
    y0 (float): Initial value of the dependent variable.
    h (float): Step size.
    n (int): Number of steps.
    
    Returns:
    tuple: Two lists containing the value of t an y.
    """
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

def plot_results(t_values, y_values):
    """
    Plots the results of the Euler method.
    
    Parameters:
    t_values (list): List of t values.
    y_values (list): List of y values.
    """
    plt.plot(t_values, y_values, label='Approximate solution (Euler method)')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.title('Solving y\' = -2y using Euler Method')
    plt.grid(True)
    plt.show()
    
def main():
    """
    Main function to set up parameters, run the Euler method, and plot results.
    """

    # Initial conditions
    t0 = 0
    y0 = 1
    h = 0.1
    n = 50
    
    # Solve the differential equation using Euler's method
    t_values, y_values = euler_method(f, t0, y0, h, n)
    
    # Plot the results
    plot_results(t_values, y_values)
    
if __name__ == "__main__":
    main()

