# inputting the data set
xg = [-1.0, 0.0, 2.0, 3.0]
yg = [-1.0, 0.0, 8.0, 27.0]

npg = len(xg)  # number of points given
print "press 'exit' to stop"

# interpolate for a input point
while True:  
    xneed = input("\nvalue at point x=")  # point of evaluation
    if xneed == exit:  # exit the loop
        break
        
    # start interpolation
    y = 0.0
    for j in range(npg):  # sum the terms
        k = 0
        m = 1.0
        # print ("ya")
        while k < npg:  # generate the term to sum
            if j != k:  # exclude the releted given point
                # multiply to generate each term
                m = m * (xneed - xg[k]) / (xg[j] - xg[k])
            k = k + 1

        y = y + m * yg[j]  # sum

    print ("value at x=%s is" % xneed, y)
