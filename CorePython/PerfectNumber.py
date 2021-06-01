'''
Program detemrines if a number N is equal to sum of its proper positive divisors(excluding itself)
First line T get no of tests
For each test, first line get N
Output-
Print YES if N is perfect no. else NP
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
'''


# Write your code here
def solution(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum == n


input_nos = input("Tests- ")

for i in range(int(input_nos)):
    number = input()
    print("YES" if solution(int(number)) else "NO")
