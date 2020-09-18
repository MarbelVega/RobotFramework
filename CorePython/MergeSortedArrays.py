# This program prints all characters in string with no. of occurences.
# Also first non-repeating character in the string

A = [1, 3, 5, 10, 34]
lenA = len(A)
B = [2, 4, 6, 7]
lenB = len(B)


def merge(A, B, lenA, lenB):
    C = []
    counterA = 0
    counterB = 0
    while counterA < lenA and counterB < lenB:
        if A[counterA] < B[counterB]:
            C.append(A[counterA])
            counterA = counterA + 1
        else:
            C.append(B[counterB])
            counterB = counterB + 1

    while counterA < lenA:
        C.append(A[counterA])
        counterA = counterA + 1

    while counterB < lenB:
        C.append(B[counterB])
        counterB = counterB + 1

    print(C)


merge(A, B, lenA, lenB)
