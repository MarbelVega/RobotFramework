# /* Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.  Handle cases like 20*/

k = 17
my_list = [10, 15, 3, 7, 2]

for i in my_list:
    diff = k - i
    if (diff in my_list) and my_list.index(i) != my_list.index(diff):
        print("Given no ", k, "is sum of ", i, "and", diff)
        my_list.remove(diff)                                      # avoid getting 2 msgs for pair found


