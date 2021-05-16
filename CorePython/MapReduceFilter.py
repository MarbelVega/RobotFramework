# All 3  functions take a function and apply to iterable

from functools import reduce

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(starts_with_A, fruit)

print(list(map_object))

# Filter returns only elements satisfying criteria

filter_obj = filter( lambda s: s[0] == 'A', fruit)
print(list(filter_obj))


list = [2, 4, 7, 3]
print(reduce(lambda x,y: x + y, list, 10))     # starts with initial value and then first elements

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results = tuple(zip(my_strings, my_numbers))

print(results)