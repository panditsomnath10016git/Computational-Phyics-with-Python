n = 100
s = 0.0
x1 = -1.0
xf = 1.0
h = (xf - x1) / (n - 1)
y = [0.0] * n

for i in range(n):
    x = x1 + (i * h)
    y[i] = (x * x) + 1
    if 0 < i < (n - 1):
        s = s + 2 * y[i]
        
sum = s + y[0] + y[n - 1]
int = (h / 2) * sum
print(int)
