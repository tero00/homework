import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x - mu*x*(1 - x)
def f(x, mu):
    return x - mu * x * (1 - x)

# Define the values of mu to plot
mu_values = [2.5, 3.0, 3.2, 3.5]
x_values = np.linspace(0.3, 1, 400)  # Define x values from 0.3 to 1


for mu in mu_values:
    y_values = f(x_values, mu)
    plt.plot(x_values, y_values, label=f'μ = {mu}')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
