from typing import List


def majorityElement(nums: List[int]) -> int:
    freq_num = {}
    for num in nums:
        freq_num[num] = 1 + freq_num.get(num, 0)

    print(freq_num)
    mode = max(freq_num, key=freq_num.get)
    print(mode)


majorityElement([3, 2, 3])
majorityElement([2, 2, 1, 1, 1, 2, 2])
