py_string = 'Python'
slice_obj = slice(1, len(py_string) - 1, 1)  # start(def=0), stop(def=length), step - stop index is not included
print(py_string[slice_obj])

print(py_string[2:] + py_string[0:2])  # shift left by 2 places

arry = [101, "%", "RED", "AIVA"];
print(arry[::-1])  # ::-1 reverses list
d = 2  # shift right so result shd be red, aiva,101,%
first = arry[0: len(arry) - d]  # d onwards elements
second = arry[len(arry) - d:]  # elements before d
second.extend(first)
print(second)

print(py_string.index("h") + py_string.endswith("on"))