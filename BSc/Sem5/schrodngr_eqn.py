
import numpy as np 
import scipy 
from scipy import integrate 
from scipy.signal import argrelextrema 
import matplotlib.pyplot as plt

l=1.0
psi0=0.0;phi0=1.0
psi_init=np.asarray([psi0,phi0])
h=l/200
x=np.arange(0.0,1+h,h)
v=np.zeros(len(x))

def Schroed(y, r, V, E):
	'''Return one dim Schroedinger 
	eqation with Potential V.'''
	psi, phi = y 
	dphidx = [phi, (V-E)*psi] 
	return np.asarray(dphidx)
	

def rk4(f, psi0, x, V, E):
 """Fourth-order Runge-Kutta method to solve 
	 phi’=f(psi,x) with psi(x[0])=psi0
	 Integrates function f with inital values psi0
	 and potenital V numerically.
	 Output is possible multidimensional (in psi) array with len(x)."""
 	n = len(x) 
 	psi = np.array([psi0]*n) 
 	for i in xrange(n -1):
	  	h = x[i+1] -x[i] 
	  	k1 = h*f(psi[i], x[i], V[i], E) 
	  	k2 = h*f(psi[i] + 0.5*k1, x[i] + 0.5*h, V[i], E) 
	  	k3 = h*f(psi[i] + 0.5*k2, x[i] + 0.5*h, V[i], E) 
	  	k4 = h*f(psi[i] + k3, x[i+1], V[i], E) 
	  	psi[i+1] = psi[i] + (k1 + 2.0*(k2 + k3) + k4) / 6.0 
	  	return psi
