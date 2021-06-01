# Given a long int find no. of ways to represent it  as sum of two of more consecutive integers
# lambda x: x + 1

def lambdaFuncdemo():
    def product(x, func): return x + func(x)
    print(product(2, lambda x: x*x))


personnel = [
    {
        "name": "Chris",
        "age": 37
    },
    {
        "name": "Susan",
        "age": 50
    }
]

# if no key given sort doesn't know which one to sort by
personnel.sort(key=lambda personnel: personnel["name"])
print(personnel)

lambdaFuncdemo()

# this prints all 4 everytime bcoz lambdas you create are referring to the current
# value of i in the active stack frame so all functions return last value of i(4)
# i is function here not integer

functions = []
for i in range(5):
    functions.append(lambda: i)

for f in functions:
    print(f())

# fix is functions.append(lambda x, i=i: x+i)
functions.clear()

for i in range(5):
    functions.append(lambda i=i: i)

for f in functions:
    print("Corrected ", f())


# array.sort() -> changes array
# sorted(arr) -> does not
