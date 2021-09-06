
# TYPES OF BUILT-IN DATA STRUCTURES IN PYTHON
# List      []       ordered | indexed | changeable | duplicates | can store diff types
# Tuple    ()       ordered | indexed | unchangeable | duplicates
# Set       {}       unordered | unindexed | no duplicates
# Dictionary  {K:V}          unordered | changeable | indexed | no duplicates
# OrderedDict - Remember insertion order


# --------------------------------LIST---------------------------------------------------------------#
numbers = list(range(1, 21, 1))      # list of numbers 1-21
number = [False] * 10     # list of 10 elements
fruits = ["apple", "mango", "pear", "grape"]
for val in fruits:
    print(val)
else:
    print("No fruits")  # for else executed at end of loop
print(set(fruits))
fruits.pop()
fruits.append("banana")  # pop and append work on last elements
print(fruits)
fruits.insert(2, "pineapple")  # elements after index shifted right
fruits.remove("mango")  # remove by value
del fruits[0]  # remove by index
fruits.sort()
print(fruits)
print("INDEX OF PEAR", fruits.index("pear"), "NEGATIVE INDEX-", fruits[-1])

print("--------------------------------TUPLE---------------------------------------------------------------")

my_tuple = ("Banana", (1, 2, 3), ["Tokyo", "London"])
# my_tuple[3] = "Cherry" not allowed
# del my_tuple[2]           cannot add/remove items in tuple but can delete entire tuple
my_tuple[2][1] = "New York"
print(my_tuple[1])  # since list is mutable we can change list items in tuple
print("Banana" in my_tuple)  # contains check
print(tuple(fruits))
print("--------------------------------SET---------------------------------------------------------------")

# unindexed so can't do set[0] etc
my_set = {"Chalk", "Duster", "Board", "pear"}
my_set.add("Pen")  # not ordered element can get inserted anywhr. same for pop
my_set.discard("Eraser")  # removes if present, no error if not
print(my_set)
my_set.add("Chalk")
print(my_set)  # no dups
set_frm_list = set(fruits)
print(set_frm_list)
print("UNION ", my_set.union(set_frm_list))  # my_set | set_frm_list
print("INTERSECTION ", my_set & set_frm_list)
print("DIFFERENCE", set_frm_list - my_set,
      "\n" "SYMMETRIC DIFFERENCE ", my_set ^ set_frm_list)

print("--------------------------------DICT--------------------------------------------------------------")

my_dict = {
    "class": "animal",
    "name": "giraffe",
    "age": 10
}
my_dict.update(age=2)  # add if not present, can also update from another dict

print(my_dict.get("name"))
print(my_dict.values())
my_dict["color"] = "grey"  # add new k:v or modify existing values
print(my_dict)

for x, y in my_dict.items():
    print(x, y)

my_dict.pop("age")
print(my_dict)
my_dict.popitem()  # remove last item
print(my_dict)
del my_dict["class"]
print(my_dict)
