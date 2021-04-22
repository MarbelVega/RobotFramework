import re


def checkAnagram(inputStr1, inputStr2):
    inputStr1 = re.sub("\\s", "", inputStr1).lower()  # regex pattern replace
    inputStr2 = re.sub("\\s", "", inputStr2).lower()
    flag = False

    if len(inputStr1) == len(inputStr2):
        for c in inputStr2:
            inputStr1 = inputStr1.replace(c, "")

        if inputStr1 == "":
            flag = True

    return flag


inputStr1 = "Mother In Lawn"
inputStr2 = "Hitler Womann"
print("ANAGRAM", checkAnagram(inputStr1, inputStr2))

# shortest would be if sorted(inputstr1) == sorted(inputstr2)
