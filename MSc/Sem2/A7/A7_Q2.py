"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 7-Q2
    
 Author : Somnath Pandit ; Date: 16.02.2021
 
"""

import numpy as np
from interpolate import lagrange_interpolate_xy

# Q2 - Lagrange interpolation in xy plane.


def f_2(x, y):
    z = x + y
    return np.sin(z) + np.cos(z)


# Get data points
n = 100  # Number of points
xi, xf = 0, np.pi
yi, yf = 0, np.pi
x_data = np.linspace(xi, xf, n / 2)
y_data = np.linspace(yi, yf, n / 2)
xx, yy = np.meshgrid(x_data, y_data)
f_data = f_2(xx, yy)

# Interpolate to find value at other point
x_0 = float(input("x value between %f & %f = " % (xi, xf)))
y_0 = float(input("y value between %f & %f = " % (yi, yf)))

f_0 = lagrange_interpolate_xy(x_data, y_data, f_data, x_0, y_0)
print("value at (%r,%r) = %.3f" % (x_0, y_0, f_0), f_2(x_0, y_0))


##OUTPUT:
# x value between 0.000000 & 3.141593 = 2.5
# y value between 0.000000 & 3.141593 = 1.5
# value at (2.5,1.5) = -1.410
