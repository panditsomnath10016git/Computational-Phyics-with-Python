"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 5
    
 Author : Somnath Pandit ; Date: 01.02.2021
 
 plotting the bessel functions J(m,x) 
""" 

import matplotlib.pyplot as plt
import numpy as np

#trapezoidal method of integration
def trapezoidal(x,y):
	h=(x[-1]-x[0])/(len(x)-1)
	s=(y[0]+2*sum(y[1:-2])+y[-1])
	return (h/2)*s

#Bessel function
def J(m,x):
    N=1000       #no. of points for trapezoidal integration
    theta= np.linspace(0,np.pi,N)
    func=np.cos(m*theta-x*np.sin(theta))
    value= trapezoidal(theta,func)
    return value/np.pi


xi,xf= 0,20                 #x range
dx=.1                       #step size for x values
xx=np.arange(xi,xf+dx,dx)   #x values
mm=[0,1,2]                  #m values

for m in mm:
    J_m=np.array([J(m,x) for x in xx])
    plt.plot(xx,J_m, label="$J_{%d}(x)$"%m)

plt.xlim(xi,xf)
plt.title("Plot of Bessel functions")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$J_{m}(x) \longrightarrow$")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("A5_Q5.png")
plt.show()

