"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 7
    
 Author : Somnath Pandit ; Date: 15.02.2021
 
"""

import matplotlib.pyplot as plt
import numpy as np
from interpolation import lagrange_interpolate, lagrange_interpolate_xy


print(50 * "-")
##Q1- Lagrange interpolation of equally spaced points in x axis.
HOLD = input(
    ">>Q1- Lagrange interpolation of equally spaced points in x axis.\n>> Press enter..."
)

def f_1(x):
    return np.sin(x)*2*np.cos(x)


# Get data points
xi,xf= 0, np.pi
x_data=np.linspace(xi,xf,10)
y_data=f_1(x_data)

# Interpolate to find value at other point
x_0=float(input("x value between %f & %f = "%(xi,xf)))
y_0=lagrange_interpolate(x_data,y_data,x_0)
print("value at %r = %.3f"%(x_0,y_0))

##Graph with 30 data points
x_data=np.linspace(xi,xf,30)
y_data=f_1(x_data)

# Interpolate to find value at other points
x_0=np.linspace(xi,xf,100)
y_0=[lagrange_interpolate(x_data,y_data,x) for x in x_0]

plt.plot(x_0,y_0,label='interpolated data')
plt.plot(x_data,y_data,'o', label='Given data')
plt.xlabel("x $\longrightarrow$")
plt.ylabel("y $\longrightarrow$")
plt.xlim(xi,xf)
plt.grid()
plt.legend()
plt.savefig("A7_Q1.svg")
plt.show()

#OUTPUT:
#x value between 0.000000 & 3.141593 = 2.5
#value at 2.5 = -0.959



print(50 * "-")#--------------------------------------------------
##Q2- Lagrange interpolation in xy plane.
HOLD = input(
    ">>Q2- Lagrange interpolation in xy plane.\n>> Press enter..."
)


def f_2(x,y):
    z=x+y
    return np.sin(z)+np.cos(z)
    
    
# Get data points
n=100  # Number of points
xi,xf= 0, np.pi
yi,yf= 0, np.pi
x_data=np.linspace(xi,xf,n/2)
y_data=np.linspace(yi,yf,n/2)
xx,yy=np.meshgrid(x_data,y_data)
f_data=f_2(xx,yy)

# Intgerpolate to find value at other point
x_0=float(input("x value between %f & %f = "%(xi,xf)))
y_0=float(input("y value between %f & %f = "%(yi,yf)))

f_0=lagrange_interpolate_xy(x_data,y_data,f_data,x_0,y_0)
print("value at (%r,%r) = %.3f"%(x_0,y_0,f_0))



##OUTPUT:
#x value between 0.000000 & 3.141593 = 2.5
#y value between 0.000000 & 3.141593 = 1.5
#value at (2.5,1.5) = -1.410



"""
print(50 * "-")#--------------------------------------------------
##Q3- statement of the question.
HOLD = input(
    ">>Q3- statement of the question.\n>> Press enter..."
)

"""
