""" COMPUTATIONAL PHYSICS LAB 
     SPRING SEM ,2021
     ASSIGNMENT 1
        
     Author : Somnath Pandit , Date : 07.01.2021
    
This program finds the n-th term of Fibonacci series and the ratio of n & n-1 th term    
 
 """

f1 = 0  # first term
f2 = 1  # second term

n = int(
    input("Number of terms in the Fibonacci series = ")
)  # taking the n value

i = 1  # initial index
f_l, f_m = f1, f2  # redifining variables for convenience

while i < n - 1:
    f_n = f_l + f_m  # next term
    f_l, f_m = f_m, f_n  # redifing the variables for the next loop
    i += 1  # updating index
#    print (f_n)       #printing from the 3rd term


if n == 1:
    f_m = 0

print("Term %d of Fibonacci series is = %d" % (n, f_m))

if n > 2:
    print("and F_%i/F_%i = %.3f" % (n, n - 1, f_m / f_l))
else:
    print("ratio can't be calculated")
