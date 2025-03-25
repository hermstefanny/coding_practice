class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                break

        a = nums[i + 1 :] + nums[: i + 1]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return None


solution = Solution()
nums = [
    0,
    1,
    2,
    4,
    5,
    6,
    7,
]
target = 6
sol = solution.search(nums, target)
print(sol)
