""" COMPUTATIONAL PHYSICS LAB 
     SPRING SEM ,2021
     ASSIGNMENT 3
        
     Author : Somnath Pandit , Date : 20.01.2021
       
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

n=.1        #distace between x points in graph

#(a) Deltoid curve
theta1=np.arange(-np.pi,np.pi+n,n)      #generating theta values
x1=2*np.cos(theta1)+np.cos(2*theta1)    #getting x values
y1=2*np.sin(theta1)-np.sin(2*theta1)    #getting y values

plt.plot(y1,x1)
plt.title("Deltoid curve")
plt.xlabel("x=$(2\cos\\theta+\cos 2\\theta)\ \longrightarrow$")
plt.ylabel("y=$(2\sin\\theta-\sin 2\\theta)\ \longrightarrow$")
plt.grid()
plt.savefig("A3_a.png")
#plt.show()



#(b) Galilean spiral
theta2=np.arange(0,10*np.pi+n,n)
r=theta2**2

x2=r*np.cos(theta2)
y2=r*np.sin(theta2)

plt.plot(y2,x2,)
plt.title("Galilean spiral\n $(r=\\theta^2)$")
plt.xlabel("x $\longrightarrow$")
plt.ylabel("y $\longrightarrow$")
plt.savefig("A3_b.png")
#plt.show()


#(c)two plots in a page
fig,(ax1,ax2)= plt.subplots(2,figsize=(6.5,8))

ax1.plot(y1,x1)
ax1.set_title("Deltoid curve")
ax1.set_xlabel("x=$(2\cos\\theta+\cos 2\\theta)\ \longrightarrow$")
ax1.set_ylabel("y=$(2\sin\\theta-\sin 2\\theta)\ \longrightarrow$")
ax1.grid()

ax2.plot(y2,x2,'-g')
ax2.set_title("Galilean spiral\n $(r=\\theta^2)$")
ax2.set_xlabel("x $\longrightarrow$")
ax2.set_ylabel("y $\longrightarrow$")
fig.tight_layout()
ax2.grid()
plt.savefig("A3_c.png")


