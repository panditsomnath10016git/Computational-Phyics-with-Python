import matplotlib.pyplot as p
np=15
y=[0.0]*np
x=[0.0]*np
for i in range(np):
	x[i]=input("x=")
	v=input("v")
	il=input("i")
	y[i]=il*v
p.plot(x,y)
p.savefig("experim.png")
