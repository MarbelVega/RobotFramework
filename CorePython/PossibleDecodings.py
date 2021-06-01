"""
Let 1 represent ‘A’, 2 represents ‘B’, etc. 
Given a digit sequence, count the number of possible decodings of the given digit sequence. 
Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"
 1 digit - can be rep in one way
 2 digits - can be rep in two ways if < 26
 3 digits - 2 + 1 ways so use fibonnocci
"""


def solution(digits, n):
    count = [0] * (n + 1)  # A table to store
    # results of subproblems
    count[0] = 1
    count[1] = 1

    for i in range(2, n + 1):

        # If the last digit is not 0, then last digit must add to the number of words

        if (digits[i - 1] > '0'):
            count[i] = count[i - 1]

        # If second last digit is smaller than 2 and last digit is smaller than 7, then
        # last two digits form a valid character
        # For 12120, count is same as 121 since 0 has to club with 2

        if (digits[i - 2] == '1' or
           (digits[i - 2] == '2' and
                digits[i - 1] < '7')):
            count[i] += count[i - 2]

    return count[n]


digits = '12120'
n = len(digits)
print("Count is ", solution(digits, n))
