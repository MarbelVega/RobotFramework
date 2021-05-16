# /* This class prints Fibonocci series where each number is the sum of the two preceding ones, starting from 0 and 1
# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
# This class prints the series upto the index and at nth index */
# Time complexity O(2^n) - Space complexity O(n)

def fib(num):
    if (num <= 1):
        return num

    else:
        return (fib(num - 1) + fib(num - 2))



def fibfor(num):
    series = [0, 1]
    for i in range(2, num):
        series.append(series[i - 1] + series[i - 2])
    return series[-1]


def fact(num):
    if (num <= 1):
        return 1
    else:
        return num * fact(num - 1)


my_list = []
for i in range(13):
    my_list.append(fib(i))
print("Fibonacci - ", my_list, my_list[-1])
print("Factorial - ", fact(7))
print(fibfor(13))
