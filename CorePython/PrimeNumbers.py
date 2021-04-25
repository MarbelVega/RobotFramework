import math

n = 31
if n == 0 or n == 1:
    print("Not prime")
else:
    for i in range(2, int(math.sqrt(n)),1):
        if n % i == 0:
            print("Not prime")
            quit()
print(n, "is prime")

