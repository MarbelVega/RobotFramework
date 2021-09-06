'''
REVERSE ARRAY WITHOUT SPECIAL CHARS
Input str = 'a,b$c' 
Output = 'c,b$a'
Only reverse chars and not $ and ,
'''


given_str = "Ab,c,de!$"
list_str = list(given_str)

length = len(given_str)
start = 0

while start < length:
    if list_str[start].isalnum():
        temp = list_str[start]

        while(True):
            length -= 1
            if list_str[length].isalnum():
                list_str[start] = list_str[length]
                list_str[length] = temp
                break

    start = start + 1

print("".join(list_str))


py_string = 'Python'
# start(def=0), stop(def=length), step - stop index is not included
slice_obj = slice(1, len(py_string) - 1, 1)
print(py_string[slice_obj])

print(py_string[2:] + py_string[0:2])  # shift left by 2 places
print("Reverse string - ", py_string[::-1])

arry = [101, "%", "RED", "AIVA"]
print(arry[::-1])  # ::-1 reverses list
d = 2  # shift right so result shd be red, aiva,101,%
first = arry[0: len(arry) - d]  # d onwards elements
second = arry[len(arry) - d:]  # elements before d
second.extend(first)
print(second)

print(py_string.index("h") + py_string.endswith("on"))
