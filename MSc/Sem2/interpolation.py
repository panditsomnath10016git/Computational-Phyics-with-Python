import numpy as np

## Lagrange interpolation ----------------------------------------


def lagrange_interpolate(x_data, f_data, x):
    n_data_points = len(x_data)
    c = np.zeros(n_data_points)

    for i in range(n_data_points):
        x_excluded = np.delete(x_data, i)
        c[i] = np.prod((x - x_excluded) / (x_data[i] - x_excluded))

    f = sum(np.multiply(c, f_data))
    return f


def lagrange_interpolate_xy(x_data, y_data, f_data, x, y):
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
    """Takes data points and interpolation points as numpy-array and retuns numpy-array of interpolated values"""
    n = len(x_data)  # number of data points
    h = np.diff(x_data)  # interval sizes
    d2f = dderivatives(x_data, f_data, h, d2f_0, d2f_n)
    f=[]
    for x in xx:
        i = find_neighbour_index(x, x_data)
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
    n = len(x_data)
    coeff_matrix = 2.0 * np.eye(n)
    coeff_matrix[0, 1] = coeff_matrix[-1, -2] = 1
    mu = h[:-1] / (h[1:] + h[:-1])
    
    for i, mu_i in zip(range(1, n - 1), mu):
        coeff_matrix[i, i - 1] = mu_i
        coeff_matrix[i, i + 1] = 1 - mu_i

    d = np.zeros(n)
    d[0] = 6 * (f_data[1] - f_data[0]) / h[0] ** 2  # or, d2f_0
    d[-1] = 6 * (f_data[-2] - f_data[-1]) / h[-1] ** 2  # or, d2f_n
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
    distance = x - x_data
    i = np.argmin(abs(distance))
    # check if i-th position is after x's position or the right-end
    if distance[i] < 0 or i == len(x_data) - 1:
        i -= 1

    return i


# ------------------------------------------------------------------
