import math as m


def f(x, y):  # define the function
    fx = 2 * x
    return fx


x0 = 0.0  # initial values
y0 = 0.0
h = 0.00001  # step size

a1 = 0.5
a2 = 1 - a1  # coefficients
q = p = 0.5 / a2
print("to stop press 'exit'")
while 1 == 1:
    h = abs(h)
    xneed = input("\nvalue at point x=")
    if xneed == exit:
        break
    np = int(abs(xneed - x0) / h)
    x = x0
    y = y0
    if xneed < x0:
        h = -h
    for i in range(np):
        k1 = h * f(x, y)
        k2 = h * f(x + p * h, y + k1 * q)
        y = y + (a1 * k1 + a2 * k2)
        x = x + h
    print
    print(y)
