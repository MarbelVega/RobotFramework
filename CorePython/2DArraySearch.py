

words = ("FOAM", "ASS");

arr = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S'],
    ['R', 'A', 'Z', 'S']
]

noOfColumns = len(arr[0])
noOfRows = len(arr)
print("Rows", noOfRows, "Columns", noOfColumns)
print('ASS' in 'MASS')


def searchWord(arr, stringSearchSequence, noOfRows, noOfColumns):
    flag = False
    for row in arr:
        rowWord = "".join(row)
        if stringSearchSequence in rowWord:
            flag = True
            break

    if flag != True:
        columnWord = ""
        a2 = zip(*arr)
        print("Zip ", a2)
    return flag




for stringSearchSequence in words:
    flag = searchWord(arr, stringSearchSequence, noOfRows, noOfColumns )
    print("search successful") if flag == True else print ("search unsuccessful")