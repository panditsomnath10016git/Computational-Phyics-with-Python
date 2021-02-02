"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 5 Q1
    
 Author : Somnath Pandit ; Date: 01.02.2021
 
 derivative of 1+0.5*tanh(2x) by central difference method
""" 

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1+0.5*np.tanh(2*x)

n=51                    #number of points
xi,xf=-2., 2.           #initial and final points
dx=(xf-xi)/(n-1)        #step size
x=np.linspace(xi,xf,n)  #x values
y=f(x)

#derivative by central difference method
df_CD= (y[2:n]-y[0:n-2])/(2*dx)

#analytic derivative 
df= 1/np.cosh(2*x)**2

#ploting
plt.plot(x[1:-1],df_CD,".",label="Central difference ")
plt.plot(x,df ,label="analytic")
plt.xlim(-2,2)
plt.title(r"Plot of $y= \frac{d}{dx} \left(1+\frac{1}{2}\tanh(2x)\right)$")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$y \longrightarrow$")
plt.legend()
plt.tight_layout()
plt.savefig("A5_Q1.png")
plt.show()


