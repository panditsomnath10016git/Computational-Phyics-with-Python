"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 4
    
 Author : Somnath Pandit ; Date: 25.01.2021
 
""" 

import matplotlib.pyplot as plt
import numpy as np

print("Press enter to see results")

## Q1
stop=input("Q1> --- \n")

eps= 1
i= 0          #counting index

while True:
    eps= eps/2
    one= 1+eps
    
    if one==1:
        print ("min eps=",eps)
        break
    i+=1
    
print ("After %d loops eps has no effect on one."%i)

# Output:
#min eps= 1.1102230246251565e-16
#After 52 loops eps has no effect on one 


## Q2  -----------------------------
stop=input("\n Q2> --- \n")

n= int(input("Input 'n' such that array length is 3*n. n= "))
print ("Length of array is = ",3*n)

init_arr= np.array([1, 2, 3])    #the repeating element 
cycl_arr= np.array([])           #initialize the cyclic array

for i in range(n):              #add the init_array n times 
    cycl_arr= np.concatenate((cycl_arr,init_arr)) 

print (cycl_arr)

# Output:
#Input 'n' such that array length is 3*n. n= 3
#Length of array is =  9
#[1. 2. 3. 1. 2. 3. 1. 2. 3.]


## Q3 -----------------------------
stop=input("\n Q3> --- \n")

m= 10
framed_one= np.zeros((m,m))  #initialize array filled with zeros

#adding 1 to border elements
index= [0,9]         #index of row or coloum to be replaced with 1
for i in index:
    framed_one[i,0:m]+=1
    framed_one[1:m-1,i]+=1
    
print(framed_one)

# Output:
#[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]


## Q4  -----------------------------
stop=input("\n Q4> --- \n")

x= np.linspace(-10,10,100)  #for contour plot
y= np.linspace(-10,10,100)

x1= np.linspace(-10,10,20)  #for gradient plot
y1= np.linspace(-10,10,20)

X,Y= np.meshgrid(x,y)
X1,Y1= np.meshgrid(x1,y1)
U  = (X**2+Y**2)/2             #potential
u,v= X1,Y1                     #gradient

# Plotting
contours= plt.contour(X,Y,U,10)              #potential plot
plt.clabel(contours, inline=1)

plt.quiver(X1,Y1,u,v)                        #gradient plot

plt.title(r"Contours of $U=\frac{1}{2} (x^2+y^2)$ and its gradient")
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$y \longrightarrow$")
plt.tight_layout
plt.savefig("A4_Q4.png",dpi=300)
plt.show()



## Q5 --------------------------------
stop=input("\nQ5> --- \n")

d=1
lmda=1
y=np.linspace(-10,10,100)
z=np.linspace(-10,10,100)

Y,Z= np.meshgrid(y,z)
V=lmda*9*np.log(((Y+d)**2+Z**2)/((Y-d)**2+Z**2)) #potential(*10^9)

contours= plt.contour(Y,Z,V,50)  #potential plot
plt.clabel(contours, inline=1)
plt.title(r"Equipotential lines of $V(x,y,z)=\frac{\lambda}{4\pi\epsilon_{0}}\ ln\left[ \frac{(y+d)^2+z^2}{(y-d)^2+z^2}\right]$ in x=0 plane"+"\n")
plt.xlabel("$y \longrightarrow$")
plt.ylabel("$z \longrightarrow$")
plt.tight_layout
plt.savefig("A4_Q5.png",dpi=300)
plt.show()




