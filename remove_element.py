from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        indeces = [i for i, item in enumerate(nums) if item == val]
        print(indeces)

        for i, index in enumerate(indeces):
            nums.pop(index)
            indeces[::] = [index - 1 for index in indeces]
            print(nums)
            print(indeces)


solution = Solution()
solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
