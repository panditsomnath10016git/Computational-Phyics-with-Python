import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data = np.loadtxt("single.txt")

x = data[:,0]
y = data[:,1]

n = len(x)
mean = sum(x*y)/n
sigma = sum(y*(x-mean)**2)/n

def gauss(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))
    
popt, pcov = curve_fit(gauss,x,y,p0=[1,mean,sigma])
x_fit = np.arange(min(x),max(x),.01)

y_fit = gauss(x_fit,*popt)

#find 5% width
y5p = y*.05
ym= abs(y-y5p)
mid_i = np.argmax(y)
x1 = np.min(x[:mid_i])
x2 = np.min(x[mid_i:])
width =x2-x1


plt.plot(x,y,".")
plt.plot(x_fit,y_fit)
plt.title("Distance vs I plot for singlemode fibre")
plt.xlabel("distance along x (mm) -->")
plt.ylabel("detector current (I mA) -->")
plt.text(11, 5, "5 %% width =%.2f mm"%width)
plt.grid()
plt.savefig("singlemode.pdf")
plt.show()

