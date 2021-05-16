# Given a long int find no. of ways to represent it  as sum of two of more consecutive integers
# lambda x: x + 1

def lambdaFuncdemo():
    product = lambda x, func: x + func(x)
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
personnel.sort(key= lambda personnel: personnel["name"])
print(personnel)

lambdaFuncdemo()

## array.sort() -> changes array
## sorted(arr) -> does not