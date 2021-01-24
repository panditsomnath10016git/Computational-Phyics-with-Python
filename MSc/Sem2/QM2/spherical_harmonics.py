""" QUANTUM MECHANICS II
     SPRING SEM ,2021
     ASSIGNMENT 1C
        
     Author : Somnath Pandit , Date : 23.01.2021

This programme plots spherical harmonics for l=2    
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np

def Y_2(m,theta,phi,real=True):
    if m==0:
        psi=np.sqrt(5/(16*np.pi))*(3*np.cos(theta)**2-1)
    if abs(m)==1:
        psi=-m*np.sqrt(15/(32*np.pi))*np.sin(2*theta)
    if abs(m)==2:
        psi=np.sqrt(15/(32*np.pi))*np.sin(theta)**2
    if real:
        return psi*np.cos(m*phi)
    if not real:
        return psi*np.sin(m*phi)

theta,phi= np.linspace(0,np.pi,50),np.linspace(0,2*np.pi,100)
THETA,PHI= np.meshgrid(theta,phi)
R= Y_2(1,THETA,PHI)

X = R * np.sin(PHI) * np.cos(THETA)
Y = R * np.sin(PHI) * np.sin(THETA)
Z = R * np.cos(PHI)

M=range(-2,2+1)
fig = plt.figure()
ax = fig.gca(projection='3d') 
plot = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
    linewidth=.005, antialiased=False, alpha=0.5)

plt.show()




