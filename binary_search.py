class Solution(object):
    def searchInsert(self, nums, target):
        # left = 0
        # right = len(nums) - 1
        # print(right)
        # root = (left + right + 1) // 2

        # if nums[root] == target:
        #     print(f"It entered here {nums[root]}")
        #     print(root)
        #     index = root
        #     return index
        # if nums[root] < target:
        #     print(
        #         f"This means that {nums[root]} is LESS than {target}, therefore i must go to the right branch"
        #     )
        #     print(f"{nums[root:right+1]}")
        #     return self.searchInsert(nums[root : right + 1], target)

        # else:
        #     print(
        #         f"This means that {nums[root]} is GREATER than {target}, therefore i must go to the left branch"
        #     )
        #     print(f"{nums[left:root]}")
        #     return self.searchInsert(nums[left:root], target)

        def binSearch(left, right):
            root = (left + right) // 2
            if left > right:
                return left
            if nums[root] == target:
                return root
            if nums[root] < target:
                print(root)
                return binSearch(root + 1, right)
            else:
                print(root)
                return binSearch(left, root - 1)

        return binSearch(0, len(nums) - 1)


solution = Solution()

nums = [1, 3, 5, 6]
target = 0

result = solution.searchInsert(nums, target)

print(f"The index is {result}")
