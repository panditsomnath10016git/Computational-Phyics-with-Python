# finding the roots of an equation by bisection method

import math as m

a = 1.0  # range of guess
b = 6.0  #
err = 2.0
eps = 0.0001  # required precision
m0 = m = (a + b) * 0.5  # initial midpoint
n = 0


def f(x):
    y = x ** 3 - 3 * x ** 2 + 1  # define the function
    return y


while err >= eps:
    if (f(a) * f(m)) < 0:
        b = m
    else:
        a = m
    m = (a + b) * 0.5
    err = abs(m0 - m)
    m0 = m
    n = n + 1

print "converged root=", m
print "no. of steps=", n
