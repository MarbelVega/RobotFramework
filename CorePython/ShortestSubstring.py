"""
Input: string = “this is a test string”, pattern = “tist”
Output: Minimum window is “t stri”
Other ways(2nd execution) of this question is -
Smallest window that contains all characters of string itself
"""

from collections import defaultdict

str = "this is a test string"
pattern = "tist"

n = len(str)
uniq_count = len(pattern)

# uniq_count = len(set(x for x in str)) in case of 2nd execution
if n < uniq_count:
    print("No such substring exists")

dict = defaultdict(lambda: 0)
dict_pattern = defaultdict(lambda: 0)
start = 0
start_index = 0
count = 0
min_len = n

for c in pattern:
    dict_pattern[c] = pattern.count(c)

print(dict_pattern)

for i in range(n):
    # count occurrence in string and putting them in dict
    dict[str[i]] += 1

    # if strings char same as pattern char

    if dict[str[i]] <= dict_pattern[str[i]]:  # dict[str[i]] == 1 for 2nd execution
        count += 1

# remove starting occurences once all chars marched

    if count == uniq_count:
        while dict[str[start]] > dict_pattern[str[start]] or dict[str[start]] == 0:
            if dict[str[start]] > dict_pattern[str[start]]:    # dict[strr[start]] > 1 for end execution
                dict[str[start]] -= 1
            start += 1

        len_window = i - start + 1

        if len_window < min_len:
            min_len = len_window
            start_index = start

if start_index == 0:
    print("No such window")

print(str[start_index: start_index + min_len])



