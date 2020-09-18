
# If user types set of keys, we want to find which key takes longest time.
# We store key and time stamp in 2D int array [[0,2],[1,5],[0,9],[2,15]
# First element of keytimes[i][0] is encoded character e.g. a=0, b=1, z=25 etc
# Second element is time when key is pressed since test started..
# So abac pressed at times 2,5,9,15 are represented above. Longest time was c in 15-9=6

keypress = [[0,2],[1,5],[0,9],[2,15]]


def getchar(keypress):
    char = keypress[0][0]
    time = keypress[0][1]
    for index in range(1, len(keypress), ):
        timediff = keypress[index][1] - keypress[index-1][1]
        if timediff > time:
            time = timediff
            char = (keypress[index][0])

    return (char+97)


c = getchar(keypress)
print(chr(c))





