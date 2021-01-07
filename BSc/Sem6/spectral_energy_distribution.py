# blackbody spectral energy distribution laws
k=8.314/6.022e23 #boltzman constant
h=6.626e-34	#plank constant
c=3.0e8	#speed of light
import numpy as np
import matplotlib.pyplot as plt

n=1000			#points for graph
T=np.array([1000.0,500.0])	#temperature
w0,wn=1.0e-5,15.0			#wavelength limit in micrometer (10^-6) 
#zero avoided for singularity in RJ formula 

w=np.linspace(w0,wn,n).reshape(n,1)
lamda=1.0e-6*w		#wavelengths
mode_density=8.0*np.pi/(lamda**4)	#density of modes
e_rj=mode_density*k*T	#Raleigh-Jeans formula
e0=h*c/lamda	#enargies at wavelengths
e_plank=mode_density*e0/(np.exp(e0/(k*T))-1)	#Plank's formula'

#compare max values of energy density at different temp.
#print max(e_plank[:,0])/max(e_plank[:,1]),T[0]/T[1]	
#plotting the graph
plt.plot(w,e_plank,w,e_rj)
plt.title("spectral energy distribution")
plt.xlabel("$\lambda (\ \mu$m$)\longrightarrow $")
plt.ylabel("Spectral energy density $\longrightarrow $ ")
plt.ylim(0,1.1*np.max(e_plank))
ref=["P(%rK)"%t for t in T]+["R-J(%rK)"%t for t in T]
plt.legend(ref) ; plt.grid()
plt.savefig("spectral energy distribution.png",dpi=400)
