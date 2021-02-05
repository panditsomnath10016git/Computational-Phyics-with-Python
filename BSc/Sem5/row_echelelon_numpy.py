# solve system of equation by forming row echelon matrix
from numpy import *

a0 = [81, 11.0, -4.0, 95]  # input the equation coefficients
a1 = [7, 52, -13, 104]
a2 = [3, 8, 29, 71]

a = matrix([a0, a1, a2], dtype=float)
# print a[0]
n = len(a0) - 1  # number of equations

for rl in range(n):  # pick leading row
    # divide the leading element to 1
    if a[rl, rl] != 0:  # check if diagonal element is non zero
        a[rl] = a[rl] / a[rl, rl]
    else:
        print "solution not available\n%r" % a
        n = 0  # for no display of solution
        break
    for rn in range(n):  # take the operational row
        if rl != rn:  # exclude the leading row
            m = a[rn, rl]  # get the subtrahend
            a[rn] -= m * a[rl]

# print a		            #'a' is the row echelon matrix
for i in range(n):  # print the solution
    print "x%r=" % i, a[i, -1]
