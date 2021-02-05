import random as rnd

n = 10
r1 = r2 = 0
i = 0

while i < n:
    x = rnd.random()
    if x <= 0.5:
        r1 = r1 + 1
    else:
        r2 = r2 + 1
    i = i + 1
    
print("no. of heads=", r1)
print("no. of tells=", r2)
