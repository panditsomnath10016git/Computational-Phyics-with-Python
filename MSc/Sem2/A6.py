"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 6
    
 Author : Somnath Pandit ; Date: 10.02.2021
 
"""

import matplotlib.pyplot as plt
import numpy as np
from simpson1_3 import simpson1_3
from quadrature import gauss_quad


print(50 * "-")
##Q1- calculate approximate value of an integral using simpson's 1/3 method
HOLD = input(
    ">>Q1 - calculate approximate value of an integral using simpson's 1/3 method.\n>> Press enter..."
)

xi, xf = 0.0, 2.0  # initial and final x value
slice_n = int(
    input("Number of slices = ")
)  # number of slices (! each parabola takes one slice)
N = 2 * slice_n + 1  # no. of points for simpson1_3 method
x = np.linspace(xi, xf, N)  # x values
y = x ** 4 - 2 * x + 1  # the integrand

numerical_val = simpson1_3(x, y)  # integration value

real_val = 4.4

err = abs((numerical_val - real_val) / real_val) * 100  # fractional error

print(
    "Value of integration is = %f \nfractional error = %f "
    % (numerical_val, err)
    + "%"
)

# OUTPUT:
# Number of slices = 100
# Value of integration is = 4.400000
# fractional error = 0.000000 %


print(50 * "-")  # ---------------------------------------------
##Q2 - Finding time period of oscillation of a particle in 1-D time independent potenial.
HOLD = input(
    ">>Q2 - Finding time period of oscillation of a particle in 1-D time independent potenial.\n>> Press enter..."
)


def V_(x):  # potential function
    k = 4.0
    return 0.5 * k * x ** 2


def integrand(X, E):
    V = np.array([V_(x) for x in X])
    return np.sqrt(2.0) / (np.sqrt(E - V))


a = -1.0
b = 1.0
epsilon = 1e-4
slices = 1e5  # no of slices for simpson 1/3 integration
N = 2 * slices + 1  # no of points for simpson 1/3 integration

# check if the function is even
is_even = 0
if V_(1.0) == V_(-1.0):
    is_even = 1

E = V_(a)  # energy
T = np.array([])  # time period

## Q2a - finding the best value of epsilon
def find_good_ln_eps(ln_eps, T):
    n = len(ln_eps)
    d_eps = ln_eps[0] - ln_eps[1]

    # derivative by central difference method
    diff_CD = (T[2:n] - T[0 : n - 2]) / (2 * d_eps)

    inflation_point_index = np.argmin(abs(diff_CD)) + 2
    ln_eps_convergent = ln_eps[inflation_point_index]
    return ln_eps_convergent, inflation_point_index


eps = np.array([])

for i in range(1, 20):
    epsilon = epsilon / 2
    eps = np.append(eps, epsilon)
    xi, xf = a + epsilon, b - epsilon
    if is_even == 1:
        xi = 0

    X = np.linspace(xi, xf, N)
    t = (1 + is_even) * simpson1_3(X, integrand(X, E))
    # print(np.log(epsilon), t)
    T = np.append(T, t)

ln_eps = np.log(eps)

good_ln_eps, index = find_good_ln_eps(ln_eps, T)
epsilon = eps[index]  # setting epsilon to the good value
print("Best value of epsilon is %r  with T = %r" % (epsilon, T[index]))

# plot of T vs ln(epsilon)
plt.plot(ln_eps, T, ".", good_ln_eps, T[index], "o")
plt.xlabel("$\ln(\epsilon) \longrightarrow$")
plt.ylabel("$ T \longrightarrow$")
plt.grid()
plt.savefig("A6_Q2a.svg")
plt.show()

## Q2b - Time period is independent of amplitude
a_min, a_max = 1, 5  # min and max amplitude
aa = np.linspace(a_min, a_max, 50)
ee = V_(aa)  # energies
tt = []

for amplitude, E in zip(aa, ee):
    xi, xf = -amplitude + epsilon, amplitude - epsilon
    if is_even == 1:
        xi = 0

    X = np.linspace(xi, xf, N)
    t = (1 + is_even) * simpson1_3(X, integrand(X, E))
    # print(t)
    tt += [t]

# plot time period vs amplitude
plt.plot(aa, tt)
plt.title("Time period vs. Amplitude")
plt.xlabel(" amplitude$ \longrightarrow$")
plt.ylabel("$ T \longrightarrow$")
plt.ylim(0, 5)
plt.grid()
plt.savefig("A6_Q2b.svg")
plt.show()


print(50 * "-")  # ---------------------------------------------
## Q3 - Find root by bisection and newton raphson method
HOLD = input(
    ">>Q3 - Find root by bisection and newton raphson method.\n>> Press enter..."
)


def f_3(x):
    return x ** 3 - x ** 2 + 2


def df_3(x):
    return 3 * x ** 2 - 2 * x


eps = float(input("Required precision = "))

while True:
    xx = np.arange(-10, 10, 0.1)
    plt.plot(xx, f_3(xx))
    plt.grid()
    plt.title("Guess the root")
    plt.show()

    # Bisection method
    print("\nBisection Method>>")
    a = float(input("min guess = "))
    b = float(input("max guess = "))
    err = 1.0  # 1st loop push
    m_i = m = (a + b) * 0.5  # initial midpoint
    n = 0  # step counter

    while err >= eps:
        if (f_3(a) * f_3(m)) < 0:
            b = m
        else:
            a = m
        m = (a + b) * 0.5
        err = abs(m_i - m)
        m_i = m
        n = n + 1

    print("converged root = ", m)
    print("no. of steps = ", n)

    # Newton raphson method
    print("\nNewton raphson method>>")
    xc = xi = float(input("Guessed root = "))  # initial guess
    err = 1.0  # 1st loop push
    n = 0  # step counter

    while err >= eps:
        x = xi - (f_3(xi) / df_3(xi))
        if xc != xi:
            err = abs(x - xi)
        xi = x
        n = n + 1

    print("converged root = ", x)
    print("no. of steps = ", n)

    another_root = str(input("Another root.. y/n? "))
    if another_root == "n" or "N":
        break

# OUTPUT:
# Required precision = .0000001
#
# Bisection Method>>
# min guess = -5
# max guess = 5
# converged root =  -1.0000000149011612
# no. of steps =  26

# Newton raphson method>>
# Guessed root = 5
# converged root =  -1.0
# no. of steps =  15

# Another root.. y/n? n


print(50 * "-")  # ---------------------------------------------
## Q4 - Heat capacity of solid by Debye's formula
HOLD = input(
    ">>Q4 - Heat capacity of solid by Debye's formula.\n>> Press enter..."
)

##Q4a - function C_v which calculates specific heat at a temp.
def C_v(T, N=1000):
    # T is temperature and N is number of points for quadrature method
    k_b = 1.38e-23  # boltzman constant
    # cosntants for Aluminium
    theta_D = 428.0  # Debye temp. in Kelvin
    rho = 6.022e28  # number density in units m^-3
    V = 1000.0  # volume of sample in units cm^3

    T_r = T / theta_D
    func = lambda x: x ** 4 * np.exp(x) / (np.exp(x) - 1) ** 2
    int_val = gauss_quad(func, 0, 1 / T_r, N=N)
    c_v = 9.0 * (V * 1e-6) * rho * k_b * T_r ** 3 * int_val

    return c_v


##Q4b - Heat capacity Vs. Temprature graph
T_min, T_max = 5.0, 500.0  # range of temperature
T = np.linspace(T_min, T_max, 100)

N = 50  # number of points for quadrature method

heat_capacity = [C_v(t, N=N) for t in T]

plt.plot(T, heat_capacity)
plt.title("Heat capacity Vs. Temprature graph")
plt.xlabel("Temperature $\longrightarrow$")
plt.ylabel("$C_{v} \longrightarrow$")
plt.grid()
plt.savefig("A6_Q4.svg")
plt.show()


print(50 * "-")  # ---------------------------------------------
## Q5 - Quantum harmonic oscillator
HOLD = input(">>Q5 - Quantum harmonic oscillator.\n>> Press enter...")

##Q5a - Quantum harmonic oscillator wavefunctions
def psi_(n, x):  # Wave-function for n-th quantum state
    N = 1.0 / (np.sqrt(2 ** n * np.math.factorial(n) * np.sqrt(np.pi)))
    return N * np.exp(-(x ** 2) / 2.0) * H_(n, x)


def H_(n, x):  # Hermite polynomials
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * H_(n - 1, x) - 2 * (n - 1) * H_(n - 2, x)


nn = range(4)  # n values
xi, xf = -4, 4  # range of x values
xx = np.linspace(xi, xf, 100)

for n in nn:
    psi_n = [psi_(n, x) for x in xx]
    plt.plot(xx, psi_n, linewidth=1.5, label="$\psi_{%d}$" % n)

plt.title("Quantum harmonic oscillator wavefunctions")
plt.xlabel("$ x \longrightarrow$")
plt.ylabel("$ \psi_{n}(x)\longrightarrow$")
plt.grid()
plt.legend()
plt.savefig("A6_Q5a.svg")
plt.show()

##Q5b - position uncertainty in n-th level of oscillator
def func(z, n=0):
    x = z / (1.0 - z)
    return x ** 2 * psi_(n, x) ** 2 * (x / z) ** 2


N = 100  # Number of points for gaussian quadrature
n = float(input("Quantum number of the state,n = "))
int_val = 2 * gauss_quad(func, 0, 1, N=N, n=n)
print("For psi_%d <x^2> = %r" % (n, np.sqrt(int_val)))
