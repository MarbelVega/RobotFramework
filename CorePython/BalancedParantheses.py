#
# Given an expression string exp, write a program to examine if its balances
# Each opening bracket should have corr closing bracket at right and vice versa.
# A paranthesis can be closed only after everything that opened after it is closed.
# E.g. [()]{}{[()()]()}  is balanced.  [(]) is not balanced
# Add opening symbols to list until we hit closing, then check if prior element is same type


pattern = '[()]{}{[()()]()}'
pattern1 = ')('
pattern2 = '[(])'

def checkbalance(pattern):
    flag = False
    stack = []
    for i in pattern:
        if i in ['(', '{', '[']:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            current = stack.pop()
            if i == ')' and current != '(':
                return False
            if i == '}' and current != '{':
                return False
            if i == ']' and current != '[':
                return False


    if not stack:
        return True

if checkbalance(pattern2):
    print("Balanced")
else:
    print("Not Balanced")