import math as mt
import matplotlib.pyplot as plt
np=500
mp=100
B=1.0
A=0.0
h=(B-A)/(np-1)
xp=[0.0]*np
yp=[0.0]*np
y0=5.0


for i in range (0,np):
        x=A+i*h
        y=5*pow(mt.e,((x**2)*0.5))
        yp[i]=y
        xp[i]=x
plt.plot (xp,yp,color='red')
#plt.savefig()

for j in range (0,mp):
        x=A+j*h
        y=y0+x*y0*h
        xp[j]=x
        yp[j]=y
        y0=y
plt.plot (xp,yp,color='blue')
plt.savefig()