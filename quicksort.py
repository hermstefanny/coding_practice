from typing import List


def pivotQuickSort(arr: List[int], left: int, right: int):
    i = left - 1
    pivot = arr[right]

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            dummy = arr[i]
            arr[i] = arr[j]
            arr[j] = dummy

    dummy_2 = arr[i + 1]
    arr[i + 1] = arr[right]
    arr[right] = dummy_2

    return i + 1


def quickSort(arr: List[int], left, right) -> List[int]:
    if left < right:
        p = pivotQuickSort(arr, left, right)
        quickSort(arr, left, p - 1)
        quickSort(arr, p + 1, right)


if __name__ == "__main__":
    arr_1 = [6, 3, 8, 5, 2, 7, 4, 1]
    quickSort(arr_1, 0, len(arr_1) - 1)
    print(arr_1)

    arr_2 = [4, 3, 2, 1]
    quickSort(arr_2, 0, len(arr_2) - 1)
    print(arr_2)

    arr_3 = [8, 9, 8, 3, 4, 3, 2, 1]
    quickSort(arr_3, 0, len(arr_3) - 1)
    print(arr_3)

    arr_4 = [100, 567, 123454, 90, 4, 0, 23, 56, 234, 907]
    quickSort(arr_4, 0, len(arr_4) - 1)
    print(arr_4)
