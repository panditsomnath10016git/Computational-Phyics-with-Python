from numpy import *


def f(x):  # define the function where the argument is a numpy array

    y = [choose(x <= 0, [-1.0, 1.0]) for x in x]
    return y


x = [-1, -0.5, 0, 0.5, 1]
print f(x)
