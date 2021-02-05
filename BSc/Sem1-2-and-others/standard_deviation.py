n = 5
a = [0.0] * n
a[0] = 5.0
a[1] = 4.0
a[2] = 2.8
a[3] = 7.9
a[4] = 6
s1 = 0.0
s2 = 0.0

for i in range(0, n):
    s1 = s1 + a[i]
avg = s1 / n

for i in range(0, n):
    s2 = s2 + pow((a[i] - avg), 2)

std = pow((s2 / n), 0.5)
print("standard deviation=", std)
