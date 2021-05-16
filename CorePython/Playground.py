import random
import string

name = 'amit' + 'y '

print(name[:2] + 'Y' + name[2:])

for i in range(len(name)):
    ## index errors if not found
    z = random.choice(string.ascii_lowercase)
    print(name[i], z,  name.index('am'), name.find(z),  name[-i-1])

print(name.replace('it', 'that'))

# Strings being immutable can;t do name[0] = 'e'

number = [False] * 10     # list of 10 elements
print(len(number))


# d[ord('A')] = True
# print(d[60:70:1])




