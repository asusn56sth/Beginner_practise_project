# Prime numbers are the numbers wich are divisible by 1 ad itself only

import math
import time


# check if the given number is prime number or not
num = int(input("Enter the number : "))

for i in range(2, round(math.sqrt(num))):
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
else:
    print(f"{num} is a prime number.")

# print all the prime numbers below 100


def check_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    sqrt_num = round(math.sqrt(num))
    for i in range(3, sqrt_num+1, 2):
        if num % i == 0:
            return False
    return True


def test(n):
    t0 = time.time()
    for i in range(1, n):
        if check_prime(i) == True:
            print(i)
    t1 = time.time()
    print("time required : ",  t1 - t0)


input("Press any key to find the list of prime numbers.")
n = int(input("Enter the upper limt for the prime numbers : "))
print(f"The prime numbers below {n} are :")

test(n)
