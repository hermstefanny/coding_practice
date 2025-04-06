from typing import List


def removeDuplis(nums: List[int]) -> int:
    indices = {}

    for i, num in enumerate(nums):
        if num not in indices.keys():
            indices[num] = [i]
        else:
            indices[num].append(i)

    index = []

    for k, v in indices.items():
        if len(v) > 1:
            index.extend(v[1:])

    print(index)

    for i in index:
        nums.pop(i)
        index[::] = [i - 1 for i in index]

    print(index)
    print(nums)


def removeDuplicates(nums: List[int]) -> int:
    j = 1
    count = 0

    for i, num in enumerate(nums):

        if nums[j] == nums[i] and count >= 1:
            print(f"conteo {count}")
            # print(f"pointr 1  {nums[j]}")
            # print(f"pointer 2  {nums[i]}")
            # print(i)
            nums.pop(i)
            count = 0

            print(f"numero   {nums[i]}")
        count += 1
        j += 1

    print(nums)


# print(removeDuplis([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(removeDuplis([1, 2, 2]))

removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
