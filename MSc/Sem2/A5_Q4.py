"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 5 Q4
    
 Author : Somnath Pandit ; Date: 01.02.2021
 
 plot of function E(x) =int_0^x exp(-t^2) dt (integrate with trapezoidal method)
""" 

import matplotlib.pyplot as plt
import numpy as np

#trapezoidal method of integtation
def trapezoidal(x,y):
	h=(x[-1]-x[0])/(len(x)-1)
	s=(y[0]+2*sum(y[1:-2])+y[-1])
	return (h/2)*s

xi,xf=0,3                       #initial and final x value
dx=0.1                           #step size
xx= np.arange(xi,xf+dx,dx)      #values of x 
E= np.array([])                 #initialize E array
N=10001                         #number of points for trapezoidal method

for x in xx:
    t= np.linspace(0,x,N)              
    y= np.exp(-t**2)            #the integrand
    int_val= trapezoidal(t,y)
    E=np.append(E,int_val)
 
plt.plot(xx,E)
plt.xlim(xi,xf)
plt.title("Plot of $E(x)=\int_{0}^{x} e^{-t^{2}} dt$\n")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$E(x) \longrightarrow$")
plt.grid()
plt.tight_layout()
plt.savefig("A5_Q4.png")
plt.show()
