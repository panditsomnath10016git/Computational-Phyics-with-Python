from pylab import *

N = 2 ** 11  # number of ensamble
n = 100  # no of toss
print N
avg = []
H = []
ensmbl = arange(N)
for exptno in ensmbl:
    nh = 0  # no. of heads
    for toss in range(n):
        rslt = random()  # tossing
        if rslt <= 0.5:
            nh = nh + 1  # counting no. of heads
    H.append(nh)
    avg.append(sum(H) / (exptno + 1.0))  # average upto that ensmbl

# 	print   " N+1,H,sum(H),avg ",exptno+1,H,sum(H),avg
# print avg[0:10],ensmbl[0:10]

plot(ensmbl, avg)
grid()
savefig("coin_toss_ensemble_avg.png")
