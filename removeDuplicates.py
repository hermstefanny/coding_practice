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
    i = 0

    # for j in range(1, len(num)): --> this caused that the j behaves in unintended ways
    while j < len(nums):

        if nums[j] == nums[i]:
            nums.pop(j)
            # nums.append(exit_num)

            j -= 1

        else:
            i += 1

        j += 1
        print(f"jota: {j}, i {i}")

    return nums


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
