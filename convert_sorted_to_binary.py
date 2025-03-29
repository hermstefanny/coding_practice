from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binary_build(self, binaryTree, node_to_insert):

        if node_to_insert > binaryTree.val:
            return self.binary_build(binaryTree.left, node_to_insert)

        if node_to_insert < binaryTree.val:
            return self.binary_build(binaryTree.right, node_to_insert)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        root_value = nums[(0 + len(nums) - 1) // 2]
        root = TreeNode(root_value)

        for num in nums:
            self.binary_build(root, num)

        return root

    def dfs_recursive(self, node, ordered_search) -> list:
        if not node:
            return
        ordered_search.append(node.val)
        self.dfs_recursive(node.left, ordered_search)
        self.dfs_recursive(node.right, ordered_search)

        return ordered_search


solution = Solution()
bin_tree_1 = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
print(bin_tree_1)
