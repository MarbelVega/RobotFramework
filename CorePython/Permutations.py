"""Given a number in the form of a list of digits, 
return all possible permutations.
The number of permutations on a set of n elements is given by  n!
"""

# Recursive function to generate all permutations of a string


def permutations(remaining, candidate=""):

    if len(remaining) == 0:
        print(candidate)

    for i in range(len(remaining)):

        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:]

        # reduce newrem one element at a time and add to newcand
        permutations(newRemaining, newCandidate)


if __name__ == '__main__':

    s = "ABC"
    permutations(s)
