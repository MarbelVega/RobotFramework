
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1
#


def solution(A):
    # write your code in Python 3.6
    i = 1
    # we could also convert the array to set for getting unique count
    A_set = set(A)
    print(A_set)
    while(i <= len(A)):
        if i not in A:
            break
        else:
            i = i + 1
    return i



A = [1, 3, 6, 4, 1, 2]
smallest = solution(A)
print(smallest)