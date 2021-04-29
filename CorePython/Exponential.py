# Given an integer n, find whether it is a power of 4 or not.
# check log of that no to base 4 i.e. math.log(n,4) is int or logn/log4(base 10) is int
# Recursilvely divide by 4 and if n%4 is non-zero and n != 1 then its not
# power of 4 will have only one bit set like 10000 etc
import math

n = 128

def power(n):
    while (n % 4 == 0):
        n = n / 4
    if n == 1:
        return True

if power(n):
    print("Yes its power of 4")
else:
    print("Not power of 4")

