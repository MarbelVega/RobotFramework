from faker import Faker
FAKER = Faker()
post_data = FAKER.paragraph(nb_sentences=5, variable_nb_sentences=True)
print("FAKER" + post_data)
print(FAKER.name() + FAKER.email())
variable = 25.1
variable_int = int(variable)  # casting
print("Casting ", variable_int)
String = "CONCATENATION"      # data type is automagically determined
print("Data type is " + String, type(String))  # + can concat str and add numbers
name = input("Enter your name")  # taking user input, always treated as string
print("Hello {}. how are ya?".format(name).capitalize())
f'Hello, {name}'   # variables inside braces are replaced with values
print (11 + 2.5)

# ------------ FOR and IF-ELSE--------------------------------------------------------------------------------#
print(String[2:4], String.lower(), String.split("T"))  # String functions ,4th element not included
arr = []
for i in range(variable_int):
    if i % 5 == 0:
        arr.append(i)
    elif i % 17 == 0:
        print("hurray prime")

print(arr)
print("MAX ELEMENT", max(arr), "ARRAY LENGTH", len(arr))

print('ASCII Code -', ord('c'))  # chr(number) to get back
