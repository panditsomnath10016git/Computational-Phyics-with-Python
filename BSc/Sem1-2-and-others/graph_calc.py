x0 = 2.6
y0 = 0.0
xsd = 0.005
ysd = 0.005

while True:
    x, y = input("x,y=")
    xn = (3 + (x / 10000.0) - x0) / xsd
    yn = ((y / 10000.0) - y0) / ysd
    print ("xn,yn=", xn, yn)
