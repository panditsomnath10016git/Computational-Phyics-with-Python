"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 5 Q3
    
 Author : Somnath Pandit ; Date: 01.02.2021
 
 Integrate a function by Trapezoidal method
""" 

import matplotlib.pyplot as plt
import numpy as np

def trapezoidal(x,y):
	h=(x[-1]-x[0])/(len(x)-1)
	s=(y[0]+2*sum(y[1:-2])+y[-1])
	return (h/2)*s

xi, xf= 0, 2                         #initial and final x value
N= int(input("Number of points = ")) #no. of points for trapezoidal method
slice_n= N-1                         #number of slices
x= np.linspace(xi,xf,N)              #x values
y= x**4-2*x+1                        #the integrand

numerical_val= trapezoidal(x,y)		#integration value
real_val= 4.4

err= abs((numerical_val-real_val)/real_val)*100    #fractional error

print("Value of integration with %d slices is = %f \nfractional error = %f "
        %(slice_n,numerical_val,err)+"%")


"""
OUTPUT:
#1
Number of points = 11
Value of integration with 10 slices is = 2.927040 
fractional error = 33.476364 %

#2
Number of points = 101
Value of integration with 100 slices is = 4.152876 
fractional error = 5.616456 %

#3
Number of points = 1001
Value of integration with 1000 slices is = 4.374130 
fractional error = 0.587944 %

"""