from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        if root.right + root.left == root.val:
            return True
        else:
            return False


tree_1 = TreeNode(10, 4, 6)
tree_2 = TreeNode(3, 5, 1)

solution = Solution()

print(solution.checkTree(tree_1))
print(solution.checkTree(tree_2))
