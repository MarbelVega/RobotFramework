import random
import string
import urllib.request
from html.parser import HTMLParser

# name = 'amit' + 'y '

# print(name[:2] + 'Y' + name[2:])

# for i in range(len(name)):
#     # index errors if not found
#     z = random.choice(string.ascii_lowercase)
#     print(name[i], z,  name.index('am'), name.find(z),  name[-i-1])

# print(name.replace('it', 'that'))

# # Strings being immutable can;t do name[0] = 'e'

# number = [False] * 10     # list of 10 elements
# print(len(number))

# intervals = [(2, 10), (3, 15), (4, 9), (8, 14), (7, 13), (5, 10), (11, 15)]
# print("Amazon")
# print(sorted([(x[0], +1) for x in intervals] + [(x[1], -1)
#       for x in intervals]))

# a = [1, 2, 3]
# list = [x*x for x in a]
# print(list)
# print("True" if 11 in list else "False")

# # d[ord('A')] = True
# # print(d[60:70:1])

# print('True' if 'abc' < 'abd' else 'False')

weburl = urllib.request.urlopen("http://www.google.com")
print(weburl.read())
