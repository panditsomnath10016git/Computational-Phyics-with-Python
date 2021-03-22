"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 8
    
 Author : Somnath Pandit ; Date: 23.02.2021
 
"""

import matplotlib.pyplot as plt
import numpy as np
from integrate import trapezoidal, simpson1_3
from interpolate import lagrange_interpolate


HOLD = input(">>Q1 - Eular-Maclaurian rule of integration.\n>> Press enter...")


def f(x):
    return x ** 4 - 2 * x + 1


def df(func, a, h=1e-5):
    return (func(a - h / 2) - func(a + h / 2)) / h


def p_error(int_value):
    x = np.linspace(a, b, 1e6 + 1)
    real_val = simpson1_3(x, f(x))

    return 100 * abs(real_val - int_value) / real_val


a, b = 0, 2
n_slice = int(input("Number of slices = "))
n = n_slice + 1  # no. of points
x = np.linspace(a, b, n)
dx = x[1] - x[0]
y = f(x)

df_a, df_b = df(f, a), df(f, b)

# Integration value
trapz_val = trapezoidal(x, y)
eular_val = trapz_val + dx ** 2 * (df_b - df_a) / 12

print("\nIntegration value by,")
print("Trapezoidal rule = %f (%.3f%% error)" % (trapz_val, p_error(trapz_val)))
print(
    "Eular-Maclaurian rule = %f (%.3f%% error)"
    % (eular_val, p_error(eular_val))
)


##OUTPUT:
# Number of slices = 10

# Integration value by,
# Trapezoidal rule = 4.506560 (2.422% error)
# Eular-Maclaurian rule = 4.399893 (0.002% error)


print(50 * "-")  # --------------------------------------------------
HOLD = input(
    ">>Q2 - Find first three bound state energies of finite square well potential.\n>> Press enter..."
)


def f_1(z, a):
    return np.tan(z * a)


def f_2(z, z_0):
    z_r = (z_0 / z) ** 2
    return 2 * np.sqrt(z_r - 1) / (2 - z_r)


def df(z, a, z_0):
    z_r = (z_0 / z) ** 2
    delta_f = np.tan(z * a) - 2 * np.sqrt(z_r - 1) / (2 - z_r)
    return delta_f


a = 1.0
z_0 = 10.0

eps = 1e-10  # Required precision
E = []  # Energy values

while True:
    xx = np.arange(-10, 10, 0.01)
    plt.plot(xx, f_1(xx, a), ".")
    plt.plot(xx, f_2(xx, z_0), ".")
    plt.ylim(-10, 10)
    plt.grid()
    plt.title("Guess the root")
    plt.xlabel("$z \\rightarrow$")
    plt.show()

    # Bisection method
    z_l = float(input("min guess = "))
    z_u = float(input("max guess = "))

    err = 1.0  # 1st loop push
    z_i = z = (z_l + z_u) * 0.5  # initial midpoint

    while err >= eps:
        if z == 0:  # tackling dividision by zero
            z = 1e-10

        if (df(z_l, a, z_0) * df(z, a, z_0)) > 0:
            z_l = z
        else:
            z_u = z

        z = (z_l + z_u) * 0.5
        err = abs(z_i - z)
        z_i = z

    print("z = ", z)
    E += [round(z ** 2 - z_0 ** 2, 3)]

    another_root = str(input("Another root.. y/n? "))
    if another_root == ("n" or "N"):
        break

print("Allowed values of energy = ", E)


##OUTPUT:
# min guess = -1
# max guess = 1
# z =  4.179233908071183e-11
# Another root.. y/n? y
# min guess = 2
# max guess = 3
# z =  2.6128800167352892
# Another root.. y/n? y
# min guess = -3
# max guess = -5
# z =  -3.9547660586540587
# Another root.. y/n? n
# Allowed values of energy =  [-100.0, -93.173, -84.36]


print(50 * "-")  # --------------------------------------------------
HOLD = input(">>Q3 - Lagrange interpolation\n>> Press enter...")


# Load the data from file
data = np.loadtxt("A8_Q3_data.txt")
x_data, y_data = data[:, 0], data[:, 1]

x = float(input("point of interpolation, x = "))
y = lagrange_interpolate(x_data, y_data, x)

print("f(%r) = %f" % (x, y))

##OUTPUT:
# x = 1.27
# f(1.27) = 0.296674


print(50 * "-")  # --------------------------------------------------
HOLD = input(
    ">>Q4 - Error dependence on no. of intervals in trapezoidal and simpson 1/3 method.\n>> Press enter..."
)


def f0(x):
    return x


def f1(x):
    return x ** 2


def f2(x):
    return x ** 3


def f3(x):
    return np.sin(x)


def rel_err(numerical_val, analytical_val):
    return abs(numerical_val - analytical_val) / analytical_val


# limits of integration
x_min = [0.0, 0.0, 0.0, 0.0]
x_max = [1.0, 1.0, 1.0, np.pi]
limits = np.array([x_min, x_max]).T

# Analytic values of integration
analytic_val = [0.5, 1.0 / 3, 1.0 / 4, 2.0]

funcs = ["$x$", "$x^2$", "$x^3$", "$\sin(x)$"]
no_of_func = len(funcs)

N = 20  # maximum interval
intervals = np.arange(2, N + 1, 2)
rules = ["trapezoidal", "simpson1_3"]

for rule in rules:
    err = np.zeros((no_of_func, len(intervals)))
    for n, n_intervals in enumerate(intervals):

        if rule == "trapezoidal":
            n_points = n_intervals + 1
        if rule == "simpson1_3":
            n_points = 2 * n_intervals + 1

        # calculate for each function
        for i, limit in enumerate(limits):
            # x values
            x = np.linspace(limit[0], limit[1], n_points)
            # y values
            y = eval("f%i(x)" % i)

            # integration values and error
            if rule == "trapezoidal":
                numeric_val = trapezoidal(x, y)
            if rule == "simpson1_3":
                numeric_val = simpson1_3(x, y)

            err[i, n] = rel_err(numeric_val, analytic_val[i])

    # print(err)
    for i, f_i in enumerate(funcs):
        plt.plot(intervals, err[i, :], label=f_i)
    plt.legend()
    plt.grid()
    plt.ylim(np.min(err) - (np.max(err) - np.min(err)) / 10, np.max(err))
    plt.xlabel("No of intervals")
    plt.title(
        "Effect of increasing intervals on integration value of different functions"
    )
    plt.ylabel("Error in %s rule" % rule)
    plt.savefig("A8_Q4_%s.svg" % rule)
    plt.show()
