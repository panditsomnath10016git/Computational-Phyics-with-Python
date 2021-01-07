import numpy as np

arr0 = np.zeros((3, 4))
print("Array filled with zeros:")
print(arr0)
print("")

arr1 = np.ones((3, 4))
print("Array filled with ones:")
print(arr1)
print("")

arrU = np.empty((3, 4))
print("Uninitialized array:")
print(arrU)
print("")

arrI = np.eye(5)
print("Identity matrix:")
print(arrI)
print("")

arrUI = np.eye(5, k=1)
print("Matrix with ones on other diagonal:")
print(arrUI)
print("")

arrR = np.arange(1, 10, 2)
print("Array generated from 1 to 10 with step 2")
print(arrR)
print("")

arrL = np.linspace(1, 10, 7)
print("Array that contains 7 numbers distributed from 1 to 10")
print(arrL)
print("")


def f(x, y):
    return x * y


arrF = np.fromfunction(f, (3, 3))
print("Array that is defined by x*y function, where x and y are indices")
print(arrF)
print("")
