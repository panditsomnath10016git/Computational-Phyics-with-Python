n = 10
N = 1000
s = 0.0
j = 0
import random as rnd

while j < N:
    h = 0
    i = 0
    while i < n:
        x = rnd.random()
        # 		print (x)
        if x < 0.5:
            h = h + 1
        i = 1 + i
    s = s + h
    j = j + 1
    
avg = s / N
print "average number of heads in", N, "\n repeatation of ", n, "\n coin tosses is=", avg
