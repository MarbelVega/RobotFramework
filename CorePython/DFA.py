"""
Given a list of words, encode each alphabet in the word(e.g a=1, z=26 etc
If sum of all chars in words is less than 100, save the word
Return all such words from smallest to largest
"""


# input_nos = input("Tests- ")
# list_words = []
# for i in range(int(input_nos)):
#     word = input()
#     list_words.append(word)

lisy = ['acalephe', 'decolor', 'estheses', 'heroize', 'paviors', 'speer', 'stower', 'tsoris', 'unmiter']

dict_scores = {}
for word in lisy:
    sum = 0
    for c in word:
        sum += ord(c.lower())-96

    print(word, sum)

    if sum < 100:
        dict_scores[word] = sum

dict_sorted = {k: v for k, v in sorted(dict_scores.items(), key=lambda item: item[1])}
print(dict_sorted)
# sort the list based on the length of strings in the list
result_list = dict_sorted.keys()
print(sorted(result_list))   # sorts alphabetically by default
print(sorted(result_list, key= len))

# acalephe, decolor, estheses, heroize, paviors, speer, stower, tsoris, unmiter
# - stower, tsoris, paviors, unmiter, estheses
    #print("YES" if solution(int(number)) else "NO")