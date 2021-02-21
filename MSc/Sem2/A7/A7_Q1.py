"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 7-Q1
    
 Author : Somnath Pandit ; Date: 15.02.2021
 
"""

import matplotlib.pyplot as plt
import numpy as np
from interpolate import lagrange_interpolate

##Q1- Lagrange interpolation of equally spaced points in x axis.


def f_1(x):
    return np.sin(x) + 2 * np.cos(x)


# Get data points
xi, xf = 0, np.pi
x_data = np.linspace(xi, xf, 10)
y_data = f_1(x_data)

# Interpolate to find value at other point
x_0 = float(input("x value between %f & %f = " % (xi, xf)))
y_0 = lagrange_interpolate(x_data, y_data, x_0)
print("value at %r = %.3f" % (x_0, y_0), f_1(x_0))

##Graph with 30 data points
x_data = np.linspace(xi, xf, 30)
y_data = f_1(x_data)

# Interpolate to find value at other points
x_0 = np.linspace(xi, xf, 100)
y_0 = lagrange_interpolate(x_data, y_data, x_0)

plt.plot(x_0, y_0, label="Interpolated data")
plt.plot(x_data, y_data, "o", label="Given data")
plt.title("Lagrange interpolation")
plt.xlabel("x $\longrightarrow$")
plt.ylabel("y $\longrightarrow$")
plt.xlim(xi, xf)
plt.grid()
plt.legend()
plt.savefig("A7_Q1.svg")
plt.show()

# OUTPUT:
# x value between 0.000000 & 3.141593 = 2.5
# value at 2.5 = -1.004
