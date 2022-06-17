# Fibonacci numbers are the sequence of the numbers, which is created by adding last two numbers

import time


# printing out the first nth finbonnacci numbers using for loop
def fibo(n):
    a, b = 1, 1
    for i in range(n):
        if i == 0:
            print(i+1, " : ", a)
        elif i == 1:
            print(i+1, " : ", b)
        elif i > 1:
            c = a + b
            if c >= n:
                break
            print(i+1, " : ", c)
            a, b = b, c


# ask user for the no of fibinacci term to get and calculate the time taken for the computer to compute.
n = int(input("How many fibonacci number do you want to see : "))
t0 = time.time()  # returns the time of start of the debuging of code
fibo(n)
t1 = time.time()  # returns the time of end of the debuging of code
print("time taken : ", t1-t0)


# ask user for the upper limit of fibinacci sequence upto which they want the sequence to build upto.
n = int(input("Enter the last number for fibonacci sequence : "))
fibo(n)
