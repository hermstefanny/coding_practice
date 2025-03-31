from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return
        root_pos = len(nums) // 2
        root = nums[root_pos]

        binary_Tree = TreeNode(
            root,
            self.sortedArrayToBST(nums[:root_pos]),
            self.sortedArrayToBST(nums[root_pos + 1 :]),
        )
        return binary_Tree

    def dfs_recursive(self, node, ordered_search) -> list:
        if not node:
            return
        ordered_search.append(node.val)
        self.dfs_recursive(node.left, ordered_search)
        self.dfs_recursive(node.right, ordered_search)

        return ordered_search


solution = Solution()

tree_dummy = solution.sortedArrayToBST([-10, -3, 0, 5, 9])

print(solution.dfs_recursive(tree_dummy, []))
