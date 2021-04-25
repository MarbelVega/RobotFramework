# Given a long int find no. of ways to represent it  as sum of two of more consecutive integers
# Input :15 # Output :3
# 15 can be represented as:
# 1+2+3+4+5
# 4+5+6
# 7+8
# The idea is to represent N as a sequence of length L+1 as:
# N = a + (a+1) + (a+2) + .. + (a+L)
# => N = (L+1)*a + (L*(L+1))/2
# => a = (N- L*(L+1)/2)/(L+1)
# We substitute the values of L starting from 1 till L*(L+1)/2 < N, if a is int then count

num = 21


def consecutive(num):
    count = 0
    l = 1
    while( l * (l-1) / 2 < num):
        a = (num - l * (l + 1) / 2) / (l+1)
        if(a.is_integer() and a != 0):
            print(a)
            count = count + 1
        l = l + 1
    return count


print(consecutive(num))
