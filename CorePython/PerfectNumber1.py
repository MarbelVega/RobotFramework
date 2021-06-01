'''
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
19 
28 = 9 + 19
37 = 9X2 + 19
46
.
82 = 9X7 + 19
91 = 9X8 + 19
100 = 9X9 + 19    -- outlier
109 = 9X10 + 19
118 = 9X11 + 19
'''


# Write your code here
def solution(n):
    base = 19
    count = 0
    list_10 = []

    while(n > count):
        sum = 0
        x = base
        while(x > 0):
            sum = sum + x % 10
            x = x // 10

        if sum == 10:
            list_10.append(base)
            count += 1

        if n == count:
            print(list_10)
            return base

        base += 9

    return -1


# input_no = input("Enter order for perfect no- ")
print(solution(15))
