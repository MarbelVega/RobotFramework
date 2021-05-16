# vowels list
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))               # def is asc

# string
py_string = 'Python'
print(sorted(py_string, reverse= True))         # reverse will do desc

second_item = [(2, 2), (3, 4), (100, 1), (1, 3)]
print(sorted(second_item, key= lambda item: item[1]))    # sorted based on second element


d1={2:'red',1:'green',3:'blue'}
print(sorted(d1.items()))  # gives back list sorted by keys
print(sorted(d1.values())) # sorted list

dict_sorted = {k: v for k, v in sorted(d1.items(), key=lambda item: item[1])}
print(dict_sorted)

l1={'carrot','vegetable','red','color','pineapple'}   # based on element length
print (sorted(l1,key=len))


# Sort by multiple keys
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)


sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)