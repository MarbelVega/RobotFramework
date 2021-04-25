#
# 1. Each word in the input string is replaced with the following: the first letter of the word, the count of distinct letters between the first and last letter, and the last letter of the word. For example, “Automotive parts" would be replaced by "A6e p3s".
# 2. A "word" is defined as a sequence of alphabetic characters, delimited by any non-alphabetic characters.
# 3. Any non-alphabetic character in the input string should appear in the output string in its original relative location.
#

import re

inputStr = "Automotive parts$whatever1x"
wordArr = re.split('[^a-zA-Z]', inputStr)
print(wordArr)

for word in wordArr:
    l = len(word)
    unique = len(set(word[1:-1]))
    if l == 1:
        inputStr = inputStr.replace(word, word[0] + str(unique))
    else:
        inputStr = inputStr.replace(word, word[0] + str(unique) + word[-1])

print(inputStr)