variable = 25.1
variable_int = int(variable)  # casting
print("Casting ", variable_int)
String = "CONCATENATION"      # data type is automagically determined
print("Data type is " + String, type(String))  # + can concat only str
print("Enter your name")
name = input()  # taking user input
print("Hello " + name)

# ------------ FOR and IF-ELSE--------------------------------------------------------------------------------#
print(String[2:4], String.lower(), String.split("T"))  # String functions
arr = []
for i in range(variable_int):
    if i % 5 == 0:
        arr.append(i)
    elif i % 17 == 0:
        print("hurray prime")

print(arr)
print("MAX ELEMENT", max(arr), "ARRAY LENGTH", len(arr))

