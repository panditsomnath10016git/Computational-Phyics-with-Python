# ! The gausswx.py file need to be present in the same directory as this.
# This program uses gaussian quadrature method to intgrate a function between two given limits
# gauss_quad(
#    function to be integrated,
#    lower limit of integration,
#    upper limit of integration,
#    N=no of points for quadrature method,
#    other argumets for the integrand function
# )

from numpy import array, sum
from gaussxw import gaussxwab


def gauss_quad(func, x_min, x_max, N=1000, **kwargs):
    xp, wp = gaussxwab(N, x_min, x_max)

    y = func(xp, **kwargs)
    int_value = sum(wp * y)

    return int_value
