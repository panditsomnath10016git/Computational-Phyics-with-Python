import math as m


def f(x, y):  # define the function
    fx = 2 * x
    return fx


x0 = 0.0  # initial values
y0 = 0.0
h = 0.001  # step size

# get values at different x
print "to stop press 'exit'"
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
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + h
    print
    print (y)
