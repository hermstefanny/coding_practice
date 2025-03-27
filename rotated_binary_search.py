class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i, num in enumerate(nums):

            if i == len(nums) - 1:
                pivot = 0

            elif nums[i] > nums[i + 1]:

                pivot = i + 1
                print(pivot)
                break

        a = nums[pivot:] + nums[:pivot]
        print(a)

        left = 0
        right = len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == a[mid]:
                return (mid + pivot) % len(nums)
            elif target < a[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1


solution = Solution()
nums = [3, 1]
target = 3
sol = solution.search(nums, target)
print(sol)
