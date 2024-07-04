import matplotlib.pyplot as plt

def f(t, y):
    return -2 * y

def euler_method(f, t0, y0, h, n):
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

t0 = 0
y0 = 1
h = 0.1
n = 50

t_values, y_values = euler_method(f, t0, y0, h, n)

plt.plot(t_values, y_values, label='Approximate solution (Euler method)')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('Solving y\' = -2y using Euler Method')
plt.grid(True)
plt.show()
