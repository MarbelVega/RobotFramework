"""
Given a sorted, rotated array
write a program to get index of given element(target) without using in-built library functions
"""

arr = [4, 5, 6, 7, 1, 2, 3]
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [10, 11, 1, 2, 3, 4, 5, 6, 7, 9]
target = 7


def binary_search(arr, target, start, end):
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


def get_index(arr):
    start_idx = 0
    end_idx = len(arr) - 1
    pivot = 0
    while start_idx < end_idx:
        if arr[start_idx] > arr[end_idx]:  # n right shift = l-n left shifts
            pivot += 1
            start_idx += 1
        else:
            print("Rotations :", pivot)
            print(arr[:pivot])
            print(arr[pivot:])
            break
            # return pivot

    # 0 to pivot and pivot to end are sorted so do regular BS

    if target in (arr[:pivot]):
        index = binary_search(arr[:pivot], target, 0, pivot - 1)
    else:
        index = pivot + binary_search(arr[pivot:], target, 0, len(arr[pivot:]) - 1)

    print(f"Index of {target} is {index}")


get_index(arr2)

#
#     if arr[start] < arr[mid]:  # if left is sorted
#         if arr[start] <= target & target < arr[mid]:  # and target lies within left and mid
#             return get_index(arr, target, start, mid - 1)
#         else:
#             return get_index(arr, target, mid + 1, end)  # element in right
#
#     else:  # right is sorted
#         if arr[mid] <= target & target < arr[end]:
#             return get_index(arr, target, mid + 1, end)  # target in mid and right
#         else:
#             return get_index(arr, target, start, mid - 1)
#
#     return -1
