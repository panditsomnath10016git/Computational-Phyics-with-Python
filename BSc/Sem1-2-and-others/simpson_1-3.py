n = 10001  # odd no . of points
s1 = s2 = 0.0
x1 = -1.0
xf = 1.0
h = (xf - x1) / (n - 1)
y = [0.0] * n

for i in range(n):
    x = x1 + i * h
    y[i] = x * x + 1
    
for i in range(0, n - 2, 2):
    s1 = s1 + y[i] + 4 * y[i + 1] + y[i + 2]

int_val = (h / 3) * s1
print(int_val)
