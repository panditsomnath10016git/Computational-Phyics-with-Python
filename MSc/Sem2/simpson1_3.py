# This program calculates the integraion value by simpson 1_3 method from given x and y array


def simpson1_3(x, y):
    h = (x[-1] - x[0]) / (len(x) - 1)
    s = y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1]

    return (h / 3) * s
