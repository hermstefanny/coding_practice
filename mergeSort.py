from typing import List


def merge(left_array: List[int], right_array: List[int]):
    merged_array = []
    i, j = 0, 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            j += 1

    while i < len(left_array):
        merged_array.append(left_array[i])
        i += 1

    while j < len(right_array):
        merged_array.append(right_array[j])
        j += 1

    return merged_array


def mergeSort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = mergeSort(arr[:mid])
    right_arr = mergeSort(arr[mid:])

    return merge(left_arr, right_arr)


print(mergeSort([6, 3, 8, 5, 2, 7, 4, 1]))
print(mergeSort([4, 3, 2, 1]))
print(mergeSort([]))
print(mergeSort([8, 9, 8, 3, 4, 3, 2, 1]))
print(mergeSort([100, 567, 123454, 90, 4, 0, 23, 56, 234, 907]))
