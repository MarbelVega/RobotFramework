
# /* This class prints Fibonocci series where each number is the sum of the two preceding ones, starting from 0 and 1
# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
# This class prints the series upto the index and at nth index */

def fib(num):
    if (num <= 1):
        return num
    else:
        return (fib(num-1) + fib(num-2))


my_list = []
for i in range(13):
    my_list.append(fib(i))
print(my_list , my_list[len(my_list)-1])


