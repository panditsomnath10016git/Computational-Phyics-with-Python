"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 7
    
 Author : Somnath Pandit ; Date: 20.02.2021
 
"""

import matplotlib.pyplot as plt
import numpy as np
from interpolation import (
    lagrange_interpolate,
    lagrange_interpolate_xy,
    cubic_spline_interpolate,
)


print(50 * "-")
HOLD = input(
    ">>Q1- Lagrange interpolation of equally spaced points in x axis.\n>> Press enter..."
)


def f_1(x):
    return np.sin(x) + 2 * np.cos(x)


# Get data points
xi, xf = 0, np.pi
x_data = np.linspace(xi, xf, 10)
y_data = f_1(x_data)

# Interpolate to find value at other point
x_0 = float(input("x value between %f & %f = " % (xi, xf)))
y_0 = lagrange_interpolate(x_data, y_data, x_0)
print("value at %r = %.3f" % (x_0, y_0))

##Graph with 30 data points
x_data = np.linspace(xi, xf, 30)
y_data = f_1(x_data)

# Interpolate to find value at other points
x_0 = np.linspace(xi, xf, 100)
y_0 = [lagrange_interpolate(x_data, y_data, x) for x in x_0]

plt.plot(x_0, y_0, label="interpolated data")
plt.plot(x_data, y_data, "o", label="Given data")
plt.xlabel("x $\longrightarrow$")
plt.ylabel("y $\longrightarrow$")
plt.xlim(xi, xf)
plt.grid()
plt.legend()
# plt.savefig("A7_Q1.svg")
plt.show()

# OUTPUT:
# x value between 0.000000 & 3.141593 = 2.5
# value at 2.5 = -1.004


print(50 * "-")  # --------------------------------------------------
HOLD = input(">>Q2- Lagrange interpolation in xy plane.\n>> Press enter...")


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
print("value at (%r,%r) = %.3f" % (x_0, y_0, f_0))


##OUTPUT:
# x value between 0.000000 & 3.141593 = 2.5
# y value between 0.000000 & 3.141593 = 1.5
# value at (2.5,1.5) = -1.410


print(50 * "-")  # --------------------------------------------------
HOLD = input(
    ">>Q3- Interpolate values from the  file_1.txt file.\n>> Press enter..."
)

# load data from the file
data = np.loadtxt("file_1.txt")
x_data, y_data = np.transpose(data[:, 0]), np.transpose(data[:, 1])
x_min, x_max = min(x_data), max(x_data)

# Interpolate to find value at pi/2
x_0 = np.pi / 2
y_0 = cubic_spline_interpolate(x_data, y_data, x_0)
print("value at %r = %.3f" % (x_0, y_0))


# Interpolate to find value at other points and plot
x_0 = np.linspace(x_min, x_max, 100)
y_0 = [cubic_spline_interpolate(x_data, y_data, x) for x in x_0]

plt.plot(x_0, y_0, "-", label="Interpolated data")
plt.plot(x_data, y_data, ".", label="Given data")
plt.xlabel("x $\longrightarrow$")
plt.ylabel("y $\longrightarrow$")
plt.xlim(x_min, x_max)
plt.ylim(0, 1.2)
plt.grid()
plt.legend()
# plt.savefig("A7_Q3.svg")
plt.show()


# Intepolate with half of the data points
x_data, y_data = x_data[0::2], y_data[0::2]

x_0 = np.pi / 2
y_0 = cubic_spline_interpolate(x_data, y_data, x_0)
print("value at %r with half data points = %.3f" % (x_0, y_0))


##OUTPUT:
# value at 1.5707963267948966 = 1.000
# value at 1.5707963267948966 with half data points = 1.000


print(50 * "-")  # --------------------------------------------------
HOLD = input(
    ">>Q4 - Interpolate with given data points and compare Lagrange and cubic spline interpolation method.\n>> Press enter..."
)

# Load the data from file
data = np.loadtxt("Q4_data.txt")
x_data, y_data = np.transpose(data[:, 0]), np.transpose(data[:, 1])

x_min, x_max = 1.0, 5.0
x = np.linspace(x_min, x_max, 100)

# Interpolate to find values between x_min and x_max
y_lagrange = [lagrange_interpolate(x_data, y_data, x) for x in x]
y_cubic_spline = [cubic_spline_interpolate(x_data, y_data, x) for x in x]

plt.plot(x_data, y_data, "o", label="Given Data")
plt.plot(x, y_lagrange, label="Lagrange interpolation")
plt.plot(x, y_cubic_spline, label="Cubic spline interpolation")
plt.title("Difference between lagrange and cubic spline interpolation")
plt.xlabel("x $\longrightarrow$")
plt.ylabel("y $\longrightarrow$")
plt.xlim(x_min, x_max)
plt.grid()
plt.legend(loc="best")
# plt.savefig("A7_Q4.svg")
plt.show()
