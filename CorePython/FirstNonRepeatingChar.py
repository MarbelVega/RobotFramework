# This program prints all characters in string with no. of occurences.
# Also first non-repeating character in the string

from collections import Counter

inputStr = "ammazon";
count = Counter(inputStr)
print(count)
# get key from value
for e in count.keys():
    if count.get(e) == 1:
        print(e)
        break

# count.items is entry set

# first non-repeating char

for c in inputStr:
    if inputStr.count(c) == 1:
        print("First unique char is " + c)
        break