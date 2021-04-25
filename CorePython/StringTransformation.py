# Livongo codility challenge
# Transform a given string by removing A and B coming together along with C and D.
# Do this until no transformations are possible. Return that string back.
# CBACD => C
# CABABD => ''
# ACBDACB => ACBDACB

def solution(S):
    checklist = ['AB', 'BA', 'CD', 'DC']
    found = False
    for item in checklist:
        if item in S:
            S = S.replace(item,'')
            found = True
            solution(S)
    return S


print(solution('AABB'))

