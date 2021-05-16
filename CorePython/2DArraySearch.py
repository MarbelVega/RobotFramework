

words = ("FOAM", "ASS", "ANNA");

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


def searchWord(arr, stringSearchSequence, noOfRows, noOfColumns = 4):
    flag = False
    for row in arr:
        rowWord = "".join(row)
        if stringSearchSequence in rowWord:
            flag = True
            break

    if flag != True:
        # needs more than one iterables but * will unzip existing iterable
        col_tuple = tuple(zip(*arr))
        for ele in col_tuple:
            columnWord = "".join(ele)
            # print("\n", columnWord)
            if stringSearchSequence in columnWord:
                flag = True
                break
    return flag


for stringSearchSequence in words:
    # note noOfColumns is not passed since its defaulted to 4
    flag = searchWord(arr, stringSearchSequence, noOfRows)
    print(stringSearchSequence)
    print("search successful") if flag == True else print ("search unsuccessful")