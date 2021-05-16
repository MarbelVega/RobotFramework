'''
Given two different sequences of the same length, a1a2...ak and b1b2...bk,
the first one is smaller than the second one for the lexicographical order,
if ai<bi (for the order of A), for the first i where ai and bi differ.
E.g abd is greater than abc and also ab.
Also return unicode diff between two strings. So abd vs abc(or ab) = 1, abc vs ram = -17
'''


str1 = 'abcd'
str2 = 'abrm'
str3 = 'ab'

print(str1 > str2)
print(str1 > str3)


def lexicographic_diff(str_1, str_2):
    min_len = min(len(str_1), len(str_2))
    for i in range(min_len):
        if str_1[i] != str_2[i]:
            return ord(str_1[i]) - ord(str_2[i])

    if len(str_1) > min_len:
        return 1
    else:
        return -1


print(lexicographic_diff(str1, str2))
# another idea is to use zip and compare each elements in tuple
