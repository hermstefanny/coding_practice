class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # k = k + (len(nums) % k)

        array_1 = nums[:-k]

        array_2 = nums[-k:]

        return array_2 + array_1


solution = Solution()
print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(solution.rotate([-1, -100, 3, 99], 2))
