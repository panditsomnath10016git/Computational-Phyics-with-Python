"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 5
    
 Author : Somnath Pandit ; Date: 01.02.2021
 
"""

import matplotlib.pyplot as plt
import numpy as np
from integrate import trapezoidal

##Q1 - derivative of 1+(1/2)*tanh(2x) by central difference method
input(
    ">>Q1 - Derivative of 1+(1/2)*tanh(2x) by central difference method\n>> Press enter..."
)


def f(x):
    return 1 + 0.5 * np.tanh(2 * x)


n = 51  # number of points
xi, xf = -2.0, 2.0  # initial and final points
dx = (xf - xi) / (n - 1)  # step size
x = np.linspace(xi, xf, n)  # x values
y = f(x)

# derivative by central difference method
df_CD = (y[2:n] - y[0 : n - 2]) / (2 * dx)

# analytic derivative
df = 1 / np.cosh(2 * x) ** 2

# ploting
plt.plot(x[1:-1], df_CD, ".", label="Central difference ")
plt.plot(x, df, label="analytic")
plt.xlim(-2, 2)
plt.title(r"Plot of $y= \frac{d}{dx} \left(1+\frac{1}{2}\tanh(2x)\right)$")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$y \longrightarrow$")
plt.legend()
plt.tight_layout()
# plt.savefig("A5_Q1.png")
plt.show()


print(20 * "-")  # -----------------------------------------------
##Q2 - numerical differentiation of the data in 'data.txt' file
input(
    ">>Q2 - Numerical differentiation of the data in 'data.txt' file\n>> Press enter..."
)


data = np.loadtxt("data.txt")  # import data from txt file
x = np.transpose(data[:, 0])
y = np.transpose(data[:, 1])

n = len(x)  # number of points
xi, xf = x.min(), x.max()  # initial and final points
dx = (xf - xi) / (n - 1)  # step size

# print(type(x),n,dx,xi,xf)

# derivative by forward difference method
diff_FWD = (y[1:n] - y[0 : n - 1]) / (dx)
last_ele = (y[-2] - y[-1]) / (-dx)  # backward diff at last point
diff_FWD = np.append(diff_FWD, last_ele)

# derivative by backward difference method
diff_BWD = (y[0 : n - 1] - y[1:n]) / (-dx)
first_ele = (y[1] - y[0]) / dx  # forward diff at first point
diff_BWD = np.insert(diff_BWD, 0, first_ele)

# derivative by central difference method
diff_CD = (y[2:n] - y[0 : n - 2]) / (2 * dx)

# ploting y vs. x
plt.plot(x, y)
plt.xlim(xi, xf)
plt.title(r"Plot of 'data.txt'")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$y \longrightarrow$")
plt.grid()
plt.tight_layout()
# plt.savefig("A5_Q2a.png")
plt.show()

# plotting derivatives
plt.plot(x, diff_FWD, label="Forward difference ")
plt.plot(x, diff_BWD, label="Backward difference ")
plt.plot(x[1:-1], diff_CD, label="Central difference ")
plt.xlim(xi, xf)
plt.title(r"Different numerical methods of differentiation")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$y \longrightarrow$")
plt.legend()
plt.grid()
plt.tight_layout()
# plt.savefig("A5_Q2b.png",dpi=300)
plt.show()


print(20 * "-")  # -----------------------------------------------
##Q3 - Integrate a function by Trapezoidal method
input(">>Q3 - Integrate a function by Trapezoidal method \n>> Press enter...")

# trapezoidal method of integtation
# def trapezoidal(x, y):
#    h = (x[-1] - x[0]) / (len(x) - 1)
#    s = y[0] + 2 * sum(y[1:-2]) + y[-1]
#    return (h / 2) * s


xi, xf = 0, 2  # initial and final x value
N = int(input("Number of points = "))  # no. of points for trapezoidal method
slice_n = N - 1  # number of slices
x = np.linspace(xi, xf, N)  # x values
y = x ** 4 - 2 * x + 1  # the integrand

numerical_val = trapezoidal(x, y)  # integration value
real_val = 4.4

err = abs((numerical_val - real_val) / real_val) * 100  # fractional error

print(
    "Value of integration with %d slices is = %f \nfractional error = %f "
    % (slice_n, numerical_val, err)
    + "%"
)


"""
OUTPUT:
#1
Number of points = 11
Value of integration with 10 slices is = 2.927040 
fractional error = 33.476364 %

#2
Number of points = 101
Value of integration with 100 slices is = 4.152876 
fractional error = 5.616456 %

#3
Number of points = 1001
Value of integration with 1000 slices is = 4.374130 
fractional error = 0.587944 %

"""


print(20 * "-")  # ------------------------------------------------
##Q4 - plot of function E(x) =int_0^x exp(-t^2) dt (integrate with trapezoidal method)
input(
    ">>Q4 - Plot of function E(x) = int_0^x exp(-t^2) dt (integrate with trapezoidal method\n>> Press enter..."
)

# trapezoidal method of integtation
# def trapezoidal(x, y):
#    h = (x[-1] - x[0]) / (len(x) - 1)
#    s = y[0] + 2 * sum(y[1:-2]) + y[-1]
#    return (h / 2) * s


xi, xf = 0, 3  # initial and final x value
dx = 0.1  # step size
xx = np.arange(xi, xf + dx, dx)  # values of x
E = np.array([])  # initialize E array
N = 10001  # number of points for trapezoidal method

for x in xx:
    t = np.linspace(0, x, N)
    y = np.exp(-(t ** 2))  # the integrand
    int_val = trapezoidal(t, y)
    E = np.append(E, int_val)

plt.plot(xx, E)
plt.xlim(xi, xf)
plt.title("Plot of $E(x)=\int_{0}^{x} e^{-t^{2}} dt$\n")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$E(x) \longrightarrow$")
plt.grid()
plt.tight_layout()
# plt.savefig("A5_Q4.png")
plt.show()


print(20 * "-")  # -----------------------------------------------
##Q5 - plotting the bessel functions J(m,x)
input(">>Q5 - Plotting the bessel functions J(m,x) \n>> Press enter...")

# Bessel function
def J(m, x):
    N = 1001  # no. of points for trapezoidal integration
    theta = np.linspace(0, np.pi, N)
    func = np.cos(m * theta - x * np.sin(theta))
    value = trapezoidal(theta, func)
    return value / np.pi


xi, xf = 0, 20  # x range
dx = 0.1  # step size for x values
xx = np.arange(xi, xf + dx, dx)  # x values
mm = [0, 1, 2]  # m values

for m in mm:
    J_m = np.array([J(m, x) for x in xx])
    plt.plot(xx, J_m, label="$J_{%d}(x)$" % m)

plt.xlim(xi, xf)
plt.title("Plot of Bessel functions")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$J_{m}(x) \longrightarrow$")
plt.legend()
plt.grid()
plt.tight_layout()
# plt.savefig("A5_Q5.png")
plt.show()
