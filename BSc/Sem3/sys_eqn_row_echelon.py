# solve system of equation by forming row echelon matrix
import numpy as np

a0 = [83.0, 11.0, -4.0, 95]  # input the equation coefficients
a1 = [7, 52, -13, 104]
a2 = [3, 8, 29, 71]

n = len(a0) - 1  # number of equations
a = [0.0] * n
for i in range(n):  # build the matrix
    an = eval("a%r" % i)
    a[i] = an
# print a

for rl in range(n):  # pick leading row
    # divide the leading element to 1
    if a[rl][rl] != 0:  # check if diagonal element is non zero
        a[rl] = [1.0 * element / a[rl][rl] for element in a[rl]]
    else:
        print ("solution not available\n%r" % a)
        n = 0  # for no display of solution
        break
    for rn in range(n):  # take the operational row
        if rl != rn:  # exclude the leading row
            m = a[rn][rl]  # get the subtrahend
            for col in range(n + 1):  # subtract coloumnwise
                a[rn][col] -= m * a[rl][col]

print (np.array(a))  #'a' is the row echelon matrix
for i in range(n):  # display the solution
    print ("x%r=" % i, a[i][n])
