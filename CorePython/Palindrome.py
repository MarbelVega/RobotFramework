

def checkPalindrome(inputStr):
    reverseStr = ""
    for i in range(len(inputStr), 0, -1):
        reverseStr += inputStr[i-1]
    print(reverseStr)
    if inputStr == reverseStr:
        return True
    else:
        return False


inputStr = "fON1I1NOF";
print("PALIDROME", checkPalindrome(inputStr))
print(''.join(sorted(inputStr)))                    # sorted returns list

# if asked to reverse without using second string, swap first,last using temp variable and iterate till length/2