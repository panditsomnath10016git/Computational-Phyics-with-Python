import math as m

n = n1 = 2  # initial number of points taken

x1 = 0.0  # limit of integration
x2 = 1.0
err = 1.0
eps = 0.0001  # required precision
x = 0.0

while err >= eps:
    y = [0.0] * n
    s = 0.0
    h = (x2 - x1) / (n - 1)

    # integrating for new 'n'
    for i in range(n):
        x = x1 + (i * h)
        y[i] = m.exp(-x * x)  # define the function
        if 0 < i < (n - 1):
            s = s + 2 * y[i]
    sum = s + y[0] + y[n - 1]
    int1 = (h / 2) * sum
    
    if n > n1:
        err = abs(int2 - int1)
    int2 = int1
    n = n + 1


print(
    "integration value= %s \nnumber\\\
 of points taken= %s \ninterval h= %s"
    % (int1, n, h)
)
