""" Solve system of equation by Gauss-seldel method define the coefficients of equations in px+qy+rz=m form such that diagonal elements are dominent and non zero  of coefficient matrix !"""

# input data
d = (95, 104, 71)  # rhs coefficients
a0 = (83.0, 11.0, -4.0)  # coefficients of x0,x1,x2...xn
a1 = (7.0, 52.0, -13.0)
a2 = (3.0, 8.0, 29.0)
n = len(d)  # number of equations
A = [0.0] * n

# build the coefficient matrix
for i in range(n):  
    A[i] = eval("a%r" % i)

xx = [0.0] * n  # initial values
eps = 0.0001  # needed accuracy
err = 1.0  # initial push value for loop
k = 0

while err >= eps:
    for i in range(n):  # take row of coefficient matrix
        s = 0.0
        for j in range(1, n):  # acessing along the row
            s = s + A[i][i - j] * xx[i - j]
        xx[i] = (d[i] - s) / A[i][i]  # get x1,x2..xn
    if k > 0:
        err = abs(xd - xx[i])
        if err == err0:  # check if loop is finite
            err = eps / 10
            print "**INVALID   SOLUTION**\n"
    err0 = err
    xd = xx[i]
    k += 1

for i in range(n):  # display solution
    print "x%i=" % i, xx[i]
print "\nno. of steps=%r \t error=%r" % (k, eps)
