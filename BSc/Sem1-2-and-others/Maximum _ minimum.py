a = [15.0 - 5, 8, -32, 87, 3, 5.6, 78.1, 679]
n = len(a)
mi = a[0]
mx = a[0]

for i in range(0, n):
    if a[i] < mi:
        mi = a[i]
    if a[i] > mx:
        mx = a[i]
        
print("max=", mx)
print("min=", mi)
