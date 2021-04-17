import numpy as np

## Lagrange interpolation ----------------------------------------


def lagrange_interpolate(x_data, f_data, xx):
    """
    Interpolate data points by Lagrange intepolation method.

    Parameters
    ------------
    x_data : numpy_array
        x values of input data.
    f_data : numpy_array
        Function values against x_data.
    xx : scalar, array_like
        Point(s) to be interpolated.

    Returns
    ---------
    values : numpy_ndarray
        Interpolated values against xx.

    """

    try:  # check if xx is array or list
        xx + [0]
    except:  # otherwise make it a list
        xx = [xx]

    n_data_points = len(x_data)
    c = np.zeros(n_data_points)
    f = []
    for x in xx:
        for i in range(n_data_points):
            x_excluded = np.delete(x_data, i)
            c[i] = np.prod((x - x_excluded) / (x_data[i] - x_excluded))

        f += [sum(np.multiply(c, f_data))]

    return np.array(f)


def lagrange_interpolate_xy(x_data, y_data, f_data, x, y):
    """
    Interpolate 2D data points by Lagrange intepolation method.

    parameters
    ------------
    x_data, y_data : numpy_arrays
        x, y values of input data.
    f_data : 2d numpy_ndarray
        Function values against (x_data, y_data).
    x, y : scalars
        Point to be interpolated.

    Returns
    ---------
    value : scalar
        Interpolated value at x.

    """

    if len(x_data) != len(y_data):
        raise Exception("x_data and y_data dimensions must match")

    n_data_points = len(x_data)
    c = np.zeros((n_data_points, n_data_points))

    for i in range(n_data_points):
        for j in range(n_data_points):
            x_excluded = np.delete(x_data, i)
            y_excluded = np.delete(y_data, j)
            c[i, j] = np.prod(
                (x - x_excluded) / (x_data[i] - x_excluded)
            ) * np.prod((y - y_excluded) / (y_data[j] - y_excluded))

    f = np.sum(np.multiply(c, f_data))

    return f


## Cubic spline interpolation ------------------------------------


def cubic_spline_interpolate(x_data, f_data, xx, d2f_0=0, d2f_n=0):
    """
    Interpolate data points by Cubic spline method.

    parameters
    ------------
    x_data : numpy_array
        x values of input data.
    f_data : numpy_array
        Function values against x_data.
    xx : scalar, array_like
        Point(s) to be interpolated.
    d2f_0 : scalar,optional
        2nd derivative at leftmost point.
    d2f_n : scalar,optional
        2nd derivative at rightmost point.

    Returns
    ---------
    values : numpy_ndarray
        Interpolated values against xx.

    """

    try:  # check if x is array or list
        xx + [0]
    except:  # otherwise make it a list
        xx = [xx]

    # Sort data
    indices = np.argsort(x_data)
    x_data, f_data = x_data[indices], f_data[indices]

    n = len(x_data)  # number of data points
    h = np.diff(x_data)  # interval sizes
    d2f = dderivatives(x_data, f_data, h, d2f_0, d2f_n)
    f = []  # f values against xx
    for x in xx:
        i = left_neighbour_index(x, x_data)
        h_i = x_data[i + 1] - x_data[i]
        A = (x - x_data[i + 1]) / (-h_i)
        B = 1 - A
        f += [
            A * f_data[i]
            + B * f_data[i + 1]
            + (A ** 3 - A) * h_i ** 2 * d2f[i] / 6
            + (B ** 3 - B) * h_i ** 2 * d2f[i + 1] / 6
        ]

    return np.array(f)


def dderivatives(x_data, f_data, h, d2f_0, d2f_n):
    """Generate continuous 2nd derivaive values at data points as needed for cubic spline method."""

    n = len(x_data)
    coeff_matrix = 2.0 * np.eye(n)
    coeff_matrix[0, 0] = coeff_matrix[-1, -1] = 1
    mu = h[:-1] / (h[1:] + h[:-1])

    for i, mu_i in enumerate(mu, 1):
        coeff_matrix[i, i - 1] = mu_i
        coeff_matrix[i, i + 1] = 1 - mu_i

    d = np.zeros(n)
    d[0] = d2f_0
    d[-1] = d2f_n
    d[1:-1] = (
        6
        * (
            (f_data[2:] - f_data[1:-1]) / h[1:]
            - (f_data[1:-1] - f_data[:-2]) / h[:-1]
        )
        / (x_data[2:] - x_data[:-2])
    )

    d2f = np.linalg.solve(coeff_matrix, d)

    return d2f


def left_neighbour_index(x, x_data):
    """Find the index of left neighbour of x in x_data."""

    distance = x - x_data
    i = np.argmin(abs(distance))
    # check if i-th position is after x's position or the right-end
    if distance[i] < 0 or i == len(x_data) - 1:
        i -= 1

    return i


# ---------------------------------------------------------------
