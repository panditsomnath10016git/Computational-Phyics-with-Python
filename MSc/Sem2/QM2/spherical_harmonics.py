""" QUANTUM MECHANICS II
     SPRING SEM ,2021
     ASSIGNMENT 1C
        
     Author : Somnath Pandit , Date : 23.01.2021

This program plots spherical harmonics for l=2    
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np

## defining the spherical harmonic function for l=2
def Y_2(m,theta,phi,real):
    if m==0:
        psi = np.sqrt(5/(16*np.pi))*(3*np.cos(theta)**2-1)
    if abs(m)==1:
        psi = -m*np.sqrt(15/(32*np.pi))*np.sin(2*theta)
    if abs(m)==2:
        psi = np.sqrt(15/(32*np.pi))*np.sin(theta)**2
    if real:
        return psi*np.cos(m*phi)
    if not real:
        return psi*np.sin(m*phi)

## taking the value of m and phase as input 
m=int(input("l=2,m= "))
if m!=0 : 
    real= bool(int(input("real=1,complex=0..? ")))
else : 
    real= True

#generating the coordinate points
theta,phi= np.linspace(0,np.pi,50),np.linspace(0,2*np.pi,100)
THETA,PHI= np.meshgrid(theta,phi)

## generating the value of the function to represent it as radial distace.
R= Y_2(m,THETA,PHI,real)

X = R * np.sin(THETA) * np.cos(PHI)
Y = R * np.sin(THETA) * np.sin(PHI)
Z = R * np.cos(THETA)

## plotting the harmonic
fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.gca(projection='3d')
#ax.view_init(30,45)
ax.axis('off')
ax.set_title(r'$Y_2^{%d}$'%m)
plot = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap=cm.rainbow,
    linewidth=0.1, antialiased=False, alpha=.85)
    
fig.tight_layout()
plt.savefig("Y_2%d_%r.png"%(m,real),dpi=250)
plt.show()
"""
#rotating view
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)
#"""




