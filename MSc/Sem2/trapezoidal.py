# This program calculates the integraion value by trapezoidal method from given x and y array


def trapezoidal(x, y):
    h = (x[-1] - x[0]) / (len(x) - 1)
    s = y[0] + 2 * sum(y[1:-2]) + y[-1]

    return (h / 2) * s
