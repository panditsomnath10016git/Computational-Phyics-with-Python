"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 5 Q2
    
 Author : Somnath Pandit ; Date: 01.02.2021
 
 numerical differentiation of the data in 'data.txt' file 
""" 

import matplotlib.pyplot as plt
import numpy as np


data=np.loadtxt("data.txt") #import data from txt file
x=np.transpose(data[:,0])
y=np.transpose(data[:,1])

n=len(x)                    #number of points
xi,xf=x.min(), x.max()      #initial and final points
dx=(xf-xi)/(n-1)            #step size

#print(type(x),n,dx,xi,xf)

#derivative by forward difference method
diff_FWD= (y[1:n]-y[0:n-1])/(dx)
last_ele= (y[-2]-y[-1])/(-dx)               #backward diff at last point
diff_FWD=np.append(diff_FWD,last_ele)

#derivative by backward difference method
diff_BWD= (y[0:n-1]-y[1:n])/(-dx)
first_ele= (y[1]-y[0])/dx                   #forward diff at first point
diff_BWD=np.insert(diff_BWD,0,first_ele)

#derivative by central difference method
diff_CD= (y[2:n]-y[0:n-2])/(2*dx)

#ploting y vs. x
plt.plot(x,y)
plt.xlim(xi,xf)
plt.title(r"Plot of 'data.txt'")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$y \longrightarrow$")
plt.grid()
plt.tight_layout()
plt.savefig("A5_Q2a.png")
plt.show()

#plotting derivatives
plt.plot(x, diff_FWD, label="Forward difference ")
plt.plot(x, diff_BWD, label="Backward difference ")
plt.plot(x[1:-1], diff_CD, label="Central difference ")
plt.xlim(xi,xf)
plt.title(r"Different numerical methods of differentiation")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$y \longrightarrow$")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("A5_Q2b.png",dpi=300)
plt.show()

