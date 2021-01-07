import numpy as np
import scipy.integrate as int
import matplotlib.pyplot as plt

n=1000			#points for graph
theta=150.0		#charecteristic temp.
t_low0,t_low1=1e-6,50	#low temp. range
t_hi0,t_hi1=1e3,5e3	#high temp. range

T_low=np.linspace(t_low0,t_low1,n)
T_hi=np.linspace(t_hi0,t_hi1,n)

f=np.concatenate((T_low,T_hi))/theta

#dulong petit
cv_0=1.0
cv_dulong=cv_0*np.ones(2*n)

#einstein
fe=1.0/f
cv_einstein=fe**2*np.exp(fe)/(np.exp(fe)-1.0)**2

#debye
f_d=lambda x: x**4*np.exp(x)/(np.exp(x)-1)**2 
F=np.array([int.quadrature(f_d,0,xm)[0] for xm in fe]) 	#int factor

cv_debye=3*f**3*F

ax1="(T/$\Theta_\mathrm{C})  \longrightarrow$"
ax2="(C$_\mathrm{v}$ /3R)  $\longrightarrow$"
ref=["Dulong-Petit","Einstein","Debye"]
#plt.subplot(211)
plt.title("Specific heats at low temperature")
plt.plot(f[:n],cv_einstein[:n],f[:n],cv_debye[:n])
plt.xlabel(ax1); plt.ylabel(ax2)
plt.legend(ref[1:])
plt.grid()
plt.savefig("specific heat theories at low temp")
plt.figure(2)
#plt.subplot(212)
plt.title("Specific heats at high temperatute")
plt.plot(f[n:],cv_dulong[n:],f[n:],cv_einstein[n:],f[n:],cv_debye[n:])
plt.xlabel(ax1); plt.ylabel(ax2)
plt.legend(ref)
plt.grid()
plt.savefig("Specific heats theories at high temp.png")
