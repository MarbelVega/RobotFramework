# Count char occureances in a string without using count
# e.g. aaabcccc = a3b1c4


str_given = 'aaabcccc'
dict_char_occurences = {}

# print('a' in dict_char_occurences)
# print(2 in dict_char_occurences)

for c in str_given:
    if c in dict_char_occurences:
        dict_char_occurences[c] = dict_char_occurences.get(c) + 1
    else:
        dict_char_occurences[c] = 1

ret_str = ''
for x, y in dict_char_occurences.items():
    ret_str += str(x) + str(y)

print(ret_str)
