def qrange(n):
    for i in range(1, n + 1):
        yield i * i


n = int(input("input the number \n"))
print("Squares of numbers from 1 to %d are:" % (n))
for i in qrange(n):
    print(i)
