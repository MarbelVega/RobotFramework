
#  Longest seq of consecutive integers -Solution works even if array is not sorted

arr = [ 32, 33, 34, 35, 36, 39, 40, 31, 42, 43, 44, 56, 92, 100, 37, 38 ]
arr_set = set(arr)
print(arr)
result = 0

for x in arr:
    count = 1
    up = x+1
    while (up in arr_set):
        count = count + 1
        arr_set.remove(up)
        up = up + 1
    down = x-1
    while(down in arr_set):
        count = count + 1
        arr_set.remove(down)
        down = down - 1

    result = max(result,count)

print("Max result ", result)

