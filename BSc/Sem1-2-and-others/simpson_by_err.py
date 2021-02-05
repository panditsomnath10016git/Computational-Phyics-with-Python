# pylint:disable=E0601
import math as m

n = n1 = 3  # initial no of points taken
x1 = 0.0
x2 = 1.0
err = 1.0
eps = 0.001  # required precision

while err >= eps:
    y = [0.0] * n
    s = 0.0
    h = (x2 - x1) / (n - 1)
    
    # getting values at different x
    for i in range(n):
        x = x1 + h * i
        y[i] = m.exp(-x * x)  # define the function
        
    # adding up using formula
    for i in range(0, n - 2, 2):
        s = s + y[i] + 4 * y[i + 1] + y[i + 2]
    int1 = (h / 3) * s
    if n > n1:
        err = abs(int2 - int1)
    int2 = int1
    n = n + 2


print(
    " integration value = %s1 \n number \\\
of points taken = %s2\n interval h = %s3"
    % (int1, n - 2, h)
)
