#pylint:disable=W0312
import math as m
import matplotlib.pyplot as plt

#setting the differential equation
'''s=susceptable , i=infected ,r= removed/recovered ,t=time '''
def f(s,i,t):	
	global beta
	dsdt=-beta*s*i
	return dsdt
def g(s,i,t):	
	global beta ; global nu
	didt=(beta*s*i)-(nu*i)
	return didt
	
'''N is total number of people in the population , 'k' is no of contacts per unit time with infected, 'tau' fraction of 'k' gets infected, 1/'nu' indicates curing time'''

N=1.3e9
k=3; tau=.58 ; b=k*tau
beta=b/N ;nu=1.0/7	
i0=10				#initially infected
s,i,t=N-i0,i0,0.0			#initial no of suceptable and infected person.
tmax=60			#total time 
dt=0.01			       # time step size

n=int(tmax/dt)	
S=[0.0]*n; I=[0.0]*n; R=[0.0]*n ;T=[0.0]*n

for j in range (n):
		S[j]=s ;I[j]=i ;R[j]=N-(s+i) ;T[j]=t
		
	#rk2 formula 
		ds1=dt*f(s,i,t)
		di1=dt*g(s,i,t)
		s1,i1,t1=s+ds1,i+di1,t+dt
		ds2=dt*f(s1,i1,t1)
		di2=dt*g(s1,i1,t1)
		s=s+(ds1+ds2)/2
		i=i+(di1+di2)/2
		t=t+dt
#		print i,s,k1,j1,k2,j2,i,t;print 
print "max no of infected = %f lakhs"%(max(I)/1e5)
#plotting the solution curve			
plt.plot(T,I,'-r',T,R,'-g',T,S)
plt.title("SIR MODEL simulation of infectious disease")
plt.xlabel("time $\longrightarrow$"); plt.ylabel("Number $\longrightarrow$")
plt.grid()
plt.legend(['Infected','Removed','Susceptible'])
plt.savefig("SIR MODEL of infectious disease")	
