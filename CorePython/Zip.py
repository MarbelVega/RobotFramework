

words = ("FOAM", "ASS", "ANNA")

arr = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S'],
    ['R', 'A', 'Z', 'S']
]

word1 = "FOAM"
word2 = "ASSN"
zippy = zip(word1, word2)
print(list(zip(*list(zippy))))

# if iterables are in another iterable unpack unzip with * operator

print(list(zip(*arr)))
