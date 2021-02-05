i = 0
a = 81
x = 1.0
n = 10

while i < n:
    x = (x + (a / x)) * 0.5
    i = i + 1
    
print(x)
