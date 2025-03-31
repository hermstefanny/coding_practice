# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bfs_with_queue(self, root: Optional[TreeNode], ordered_search) -> list:
        if not root:
            return
        traversed = deque([root])

        while traversed:
            node = traversed.popleft()
            print(f"traversce queue {traversed}")
            print(node.val)
            ordered_search.append(node.val)

            if node.left:
                traversed.append(node.left)
            if node.right:
                traversed.append(node.right)

        return ordered_search

    def bfs_with_recursion(self, node: Optional[TreeNode], ordered_search) -> list:

        if not node:
            return

        traversed = deque([node])
        print(traversed)
        node = traversed.popleft()
        ordered_search.append(node.val)

        self.bfs_with_recursion(node.left, ordered_search)
        self.bfs_with_recursion(node.right, ordered_search)

        return ordered_search

    def dfs_recursive(self, node, ordered_search) -> list:
        if not node:
            return
        ordered_search.append(node.val)
        self.dfs_recursive(node.left, ordered_search)
        self.dfs_recursive(node.right, ordered_search)

        return ordered_search

    def minDepth(self, root: Optional[TreeNode]) -> int:
        count = 0

        def search(root, count):
            if not root:
                return count
            count += 1

            count_left = search(root.left, count)

            count_right = search(root.right, count)

            if count_left <= count_right:
                count = count_left
            else:
                count = count_right

            return count

        return search(root, count)


solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(solution.minDepth(root))
# print(solution.bfs_with_queue(root, []))
# print(solution.bfs_with_recursion(root, []))
