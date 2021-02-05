import cmath as m


def fx(x):
    y = x ** 2
    z = x ** 0.5
    return y, z


a = float(input("enter x="))

sol = fx(a)
print(sol)
