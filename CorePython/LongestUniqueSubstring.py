# Check if string is uniq until given length

str = "how are you amit? fine ? "
no_places = 8

# replace substring
print(str.replace("amit","intellij"))
i = str.index("you")               # can use str.find also but it errors if not found
print(str[0:i]+"we"+ str[i+3:])       # without using replace

# find no of occurances of a substring or char
print(len(str.split(" "))-1, '=', str.count(" "))

# strip last 2 char
print(str.rstrip("? "))

'''
Longest substring containing of unique chars = shortest substring containing all chars ?
'''


string1 = "amazonm"
string = "aaab"
seen = {}
maximum_length = 0

# starting the inital point of window to index 0
start = 0

for end in range(len(string)):
    # Checking if we have already seen the element or not
    if string[end] in seen:

        # If we have seen the number, move the start pointer
        # to position after the last occurrence
        start = max(start, seen[string[end]] + 1)

        # Updating the last seen value of the character
    seen[string[end]] = end
    maximum_length = max(maximum_length, end-start + 1)
print(seen)
print("Longest Substring Without Repeating Characters" , maximum_length, string[start:end + 1])