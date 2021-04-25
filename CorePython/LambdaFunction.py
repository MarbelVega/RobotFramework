# Given a long int find no. of ways to represent it  as sum of two of more consecutive integers
# lambda x: x + 1

def lambdaFuncdemo():
    product = lambda x, func: x + func(x)
    print(product(2, lambda x: x*x))

