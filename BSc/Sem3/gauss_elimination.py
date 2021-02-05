# solve system of equation by Gauss elimination method

a0 = [1, -1, 4, 5]  # input the equations
a1 = [2, -3, 8, 4]
a2 = [1, -2, 4, 9]

n = len(a0) - 1  # number of equations
a = [0.0] * n

# build the matrix
for i in range(n):  
    an = eval("a%r" % i)
    a[i] = an

# make upper triangular matrix
for rl in range(n):  # pick leading row
    # divide the leading element to 1
    if a[rl][rl] != 0:  # isdiagonal element non-zero ?
        a[rl] = [1.0 * element / a[rl][rl] for element in a[rl]]
    else:
        print "(*_*)\n\nsolution is not available\n%r" % a
        n = 0  # for no display of solution
        break
    for rn in range(n):  # take the operational row rn
        if rn > rl:  # rn is under leading row
            m = a[rn][rl]  # get the multiplier
            for col in range(n + 1):  # columnwise rn-(m*rl)
                a[rn][col] -= m * a[rl][col]

# find the solutions
xx = [0.0] * n
i = n - 1
while i >= 0:  # climbing from lowest row
    s = 0.0
    for j in range(n):  # multiply each element in coefficient matrix's' row...
        s = s + a[i][j] * xx[j]  # with associated unknown x
    xx[i] = a[i][-1] - s
    i = i - 1
# print a    	#'a' is the upper triangular matrix

# display the solutions
for s in range(n):
    print "x%r= %r" % (s, xx[s])
