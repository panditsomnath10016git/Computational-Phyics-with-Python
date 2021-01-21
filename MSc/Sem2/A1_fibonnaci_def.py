""" COMPUTATIONAL PHYSICS LAB 
     SPRING SEM ,2021
     ASSIGNMENT 1
        
     Author : Somnath Pandit , Date : 07.01.2021
    
This program finds the n-th term of Fibonacci series and the ration of n & n-1 th term using def function
 
 """
def fib(f_l,f_m,n):

    f_n= f_l+f_m
    
        
f1=0                #first term
f2=1                #second term

n=int(input("Number of terms in the Fibonacci series = ")) #taking the n value


    
print ("The %d-th term of Fibonacci series is = %d"%(n,f_n))
print ("and F_%i/F_%i = %.3f"%(n,n-1,f_m/f_l))


