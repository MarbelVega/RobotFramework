"""
Given a sorted, rotated array
write a program to get index of given element(target) without using in-built library functions
"""

arr = [4, 5, 6, 7, 1, 2, 3]
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [11, 1, 2, 3, 4, 5, 6, 7, 9]
target = 5


# start_idx = 0
# end_idx = end
# pivot = -1
# while start_idx < end_idx:
#     if arr[start_idx] > arr[end_idx]:    # n right shift = l-n left shifts
#         pivot += 1
#         start_idx += 1
#     else:
#         print("Pivot Index :", pivot)
#         break


def get_index(arr, target, start, end):

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    if arr[start] < arr[mid]:  # if left is sorted
        if arr[start] <= target & target < arr[mid]:  # and target lies within left and mid
            return get_index(arr, target, start, mid - 1)
        else:
            return get_index(arr, target, mid + 1, end)  # element in right

    else:  # right is sorted
        if arr[mid] <= target & target < arr[end]:
            return get_index(arr, target, mid + 1, end)  # target in mid and right
        else:
            return get_index(arr, target, start, mid - 1)

    return -1


print(get_index(arr, target, 0, len(arr) - 1))
