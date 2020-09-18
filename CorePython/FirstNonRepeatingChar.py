# This program prints all characters in string with no. of occurences.
# Also first non-repeating character in the string

from collections import Counter

inputStr = "ammazon";
count = Counter(inputStr)
print(count)
print(reversed(inputStr))
for e in count:
    if count[e] == 1:
        print(e)
        break


