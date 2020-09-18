# Check if string is uniq until given length
from locust import HttpUser,task

str = "how are you amit? fine ? "
no_places = 8

print(str.replace("amit","intellij"))
i = str.index("you")
print(str[0:i]+"we"+ str[i+3:])       # without using replace

# find no of occurances of a substring

print(len(str.split(" "))-1)

string = "acbbxyz"

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
print("Max length of uniq chars" , maximum_length)