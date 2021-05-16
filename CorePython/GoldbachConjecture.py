#Given an even number (greater than 2),
# return two prime numbers whose sum will be equal to the given number.
from typing import List, Any

n = 128

prime_numbers = list(range(3,n,2))
#print(prime_numbers)

for p in prime_numbers:
    i = p*p
    while(i <= n):
        prime_numbers.remove(i) if i in prime_numbers else 0
        i += p

print(prime_numbers)
print(lambda prime_numbers: prime_numbers[0])

for p_num in prime_numbers:
    diff = n - p_num
    if diff in prime_numbers:
        print(p_num, diff)
        prime_numbers.remove(p_num)

