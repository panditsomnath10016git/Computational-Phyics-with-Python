# finding the roots of an equation by newton raphson method

xc = x0 = -2.0  # initial guess
err = 1.0
eps = 0.0001  # required precision
n = 0

while err >= eps:
    f = pow(x0, 3) - 3 * x0 * x0 + 1  # define the function
    df = 3 * x0 * x0 - 6 * x0  # derivative of the function
    x = x0 - (f / df)
    if xc != x0:
        err = abs(x - x0)
    x0 = x
    n = n + 1
    
print("converged root=", x)
print("no. of steps=", n)
