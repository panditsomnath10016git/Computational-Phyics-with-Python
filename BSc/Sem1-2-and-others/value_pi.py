n = 2
s1 = 1.0
s2 = 1.0
sum = 0.0

for i in range(0, n):
    p = (26390.0 * i) + 1103.0
    q = pow(396.0, 4 * i)
    for j in range(1, (4 * i) + 1):
        s1 = s1 * j
    for k in range(1, i + 1):
        s2 = s2 * k
    f = s1 / pow(s2, 4)
    sum = sum + (f * (p / q))
    
ans = (pow(8.0, 0.5) / 9801) * sum
pi = 1.0 / ans
print pi
