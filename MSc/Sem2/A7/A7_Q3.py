"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 7-Q3
    
 Author : Somnath Pandit ; Date: 15.02.2021
 
"""

import matplotlib.pyplot as plt
import numpy as np
from interpolate import cubic_spline_interpolate

# Q3 - Interpolate values from the  file_1.txt file

# load data from the file
data = np.loadtxt("file_1.txt")
x_data, y_data = data[:, 0], data[:, 1]
x_min, x_max = min(x_data), max(x_data)

# Interpolate to find value at pi/2
x_0 = np.pi / 2
y_0 = cubic_spline_interpolate(x_data, y_data, x_0)
print("value at %r = %.3f" % (x_0, y_0))


# Interpolate to find value at other points and plot
x_0 = np.linspace(x_min, x_max, 100)
y_0 = cubic_spline_interpolate(x_data, y_data, x_0)

plt.plot(x_0, y_0, "-", label="Interpolated data")
plt.plot(x_data, y_data, ".", label="Given data")
plt.title("Cubic spline interpolation of data in file_1.txt")
plt.xlabel("x $\longrightarrow$")
plt.ylabel("y $\longrightarrow$")
plt.xlim(x_min, x_max)
plt.ylim(0, 1.2)
plt.grid()
plt.legend()
plt.savefig("A7_Q3.svg")
plt.show()


# Intepolate with half of the data points
x_data, y_data = x_data[0::2], y_data[0::2]

x_0 = np.pi / 2
y_0 = cubic_spline_interpolate(x_data, y_data, x_0)
print("value at %r with half data points = %.3f" % (x_0, y_0))


##OUTPUT:
# value at 1.5707963267948966 = 1.000
# value at 1.5707963267948966 with half data points = 1.000
