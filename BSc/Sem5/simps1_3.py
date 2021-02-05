from numpy import *

nint = 101  # odd no of points
ri, rf = -1.0, 1.0  # function range

xint = linspace(ri, rf, nint, dtype=float)  # x value for integration


def simps1_3(ya, xa):
    h = (xa[-1] - xa[0]) / (len(xa) - 1)
    s = ya[0] + 4 * sum(ya[1:-2:2]) + 2 * sum(ya[2:-3:2]) + ya[-1]
    return (h / 3) * s


print simps1_3(cos(xint), xint)
