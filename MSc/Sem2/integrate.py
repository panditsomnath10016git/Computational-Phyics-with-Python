# !! The gausswx.py file need to be present in the same directory as this integrate.py.

from numpy import sum
from gaussxw import gaussxwab


def gauss_quad(func, x_min, x_max, N=1000, **kwargs):
    """
    Gaussian quadrature method to integrate a function between two given limits.

    Parameters
    ------------
    func : function
        Function to be integrated.
    x_min : scalar
        Lower limit of integration.
    x_max : scalar
        Upper limit of integration.
    N : int,optional
        Number of points for quadrature method.
    **kwargs :
        Extra arguments for the integrand function func.

    Returns
    ---------
    value : scalar
        Integration value.

    """

    xp, wp = gaussxwab(N, x_min, x_max)

    y = func(xp, **kwargs)
    int_value = sum(wp * y)

    return int_value


def trapezoidal(x, y):
    """
    Trapezoidal method to integrate given data.

    Parameters
    ------------
    x : array_like
        Linearly spaced x values.
    y : array_like
        y = f(x) values.

    Returns
    ---------
    value : scalar
        Integration value.

    """

    h = x[1] - x[0]
    s = y[0] + 2 * sum(y[1:-1]) + y[-1]

    return (h / 2) * s


def simpson1_3(x, y):
    """
    Simpson 1/3 method to integrate given data.

    Parameters
    ------------
    x : array_like
        Linearly spaced x values. Odd no of values are needed.
    y : array_like
        y = f(x) values.

    Returns
    ---------
    value : scalar
        Integration value.

    """
    if len(x) % 2 == 0:
        raise ValueError(
            "Number of points must be odd for simpson 1/3 integration"
        )

    h = x[1] - x[0]
    s = y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1]

    return (h / 3) * s
