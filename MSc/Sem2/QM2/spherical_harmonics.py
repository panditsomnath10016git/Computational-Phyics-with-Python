""" QUANTUM MECHANICS II
     SPRING SEM ,2021
     ASSIGNMENT 1C
        
     Author : Somnath Pandit , Date : 23.01.2021

This program plots spherical harmonics for l=1,2    
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np

## defining the spherical harmonic function for l=1,2
def SpHarmonics(l,m,theta,phi,real=True):
    if l==1:
        if m==0:
            psi = np.sqrt(3/(4*np.pi))*np.cos(theta)
        if abs(m)==1:
            psi = -m*np.sqrt(3/(8*np.pi))*np.sin(theta)
     #   print(psi)
    if l==2:
        if m==0:
            psi = np.sqrt(5/(16*np.pi))*(3*np.cos(theta)**2-1)
        if abs(m)==1:
            psi = -m*np.sqrt(15/(32*np.pi))*np.sin(2*theta)
        if abs(m)==2:
            psi = np.sqrt(15/(32*np.pi))*np.sin(theta)**2
    
    if m==0:
        phase = ""
        Y_lm = psi
    else:
        if real:
            Y_lm = psi*np.cos(m*phi)
            phase = "Re"
        else:
            Y_lm = psi*np.sin(m*phi)
            phase = "Im"
    return Y_lm, phase

# taking the value of m and phase as input
l= int(input("l= 1 or 2..?\n>> ")) 
mm= np.arange(-l,l+1)

print("l=",l,"\nm=",mm)

# generating the coordinate points
theta,phi= np.linspace(0,np.pi,51),np.linspace(0,2*np.pi,101)
THETA,PHI= np.meshgrid(theta,phi)

for m in mm:
    if m==0: 
        REAL= [True]
    else: 
        REAL= [True,False]

    for real in REAL:
        # generating the value of the function to represent it as radial distace.
        Y_lm , phase = SpHarmonics(l,m,THETA,PHI,real)
        R = abs(Y_lm)
        X = R * np.sin(THETA) * np.cos(PHI)
        Y = R * np.sin(THETA) * np.sin(PHI)
        Z = R * np.cos(THETA)


        # plotting the harmonics
        fig = plt.figure(figsize=plt.figaspect(.75))
        ax = fig.gca(projection='3d')
        if m==0:
            ax.view_init(20)

        #ax.axis('off')
        ax.set_title("Plot of  r=|"+phase+
            '$\left(Y_{%d}^{%d}(\\theta,\phi)\\right)$|'%(l,m),
            fontsize=20)
        fcolor=cm.ScalarMappable(cmap=plt.get_cmap('rainbow'))
        plot = ax.plot_surface(
            X, Y, Z, rstride=1, cstride=1, 
            facecolors=fcolor.to_rgba(Y_lm),
            linewidth=0.5, antialiased=True, alpha=1)
        ax.set_xlabel("$x \\rightarrow$",fontsize=20)
        ax.set_ylabel("$y \\rightarrow$",fontsize=20) 
        ax.set_zlabel("$z \\rightarrow$",fontsize=20) 
        fig.tight_layout()
        print(l,m,phase)
        fcolor.set_array(Y_lm)
        fig.colorbar(fcolor,shrink=.5,
            label=phase+'$(Y_{%d}^{%d})$'%(l,m))
        plt.savefig("%sY_%d%d.png"%(phase,l,m))
        #plt.show()
        """
        # rotating view
        for angle in range(0, 360):
            ax.view_init(30, angle)
            plt.draw()
            plt.pause(.001)
        """




