"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 7-Q4
    
 Author : Somnath Pandit ; Date: 20.02.2021
 
"""

import matplotlib.pyplot as plt
import numpy as np
from interpolate import lagrange_interpolate, cubic_spline_interpolate

# Q4 - Interpolate with given data points and compare Lagrange and cubic spline interpolation method.

# Load the data from file
data = np.loadtxt("A7_Q4_data.txt")
x_data, y_data = data[:, 0], data[:, 1]

x_min, x_max = min(x_data), max(x_data)
x = np.linspace(x_min, x_max, 100)

# Interpolate to find values between x_min and x_max
y_lagrange = lagrange_interpolate(x_data, y_data, x)
y_cubic_spline = cubic_spline_interpolate(x_data, y_data, x)

plt.plot(x_data, y_data, "o", label="Given Data")
plt.plot(x, y_lagrange, label="Lagrange interpolation")
plt.plot(x, y_cubic_spline, label="Cubic spline interpolation")
plt.title("Difference between Lagrange and Cubic spline interpolation")
plt.xlabel("x $\longrightarrow$")
plt.ylabel("y $\longrightarrow$")
plt.xlim(x_min, x_max)
plt.grid()
plt.legend(loc="best")
plt.savefig("A7_Q4.svg")
plt.show()
