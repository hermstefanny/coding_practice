from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs_with_stack(self, root, ordered_search) -> list:
        if not root:
            return
        traversed = [root]
        while traversed:
            node = traversed.pop()
            print(node.val)
            ordered_search.append(node.val)

            if node.right:
                traversed.append(node.right)
            if node.left:
                traversed.append(node.left)

        return ordered_search

    def dfs_recursive(self, node, ordered_search) -> list:
        if not node:
            return
        ordered_search.append(node.val)
        self.dfs_recursive(node.left, ordered_search)
        self.dfs_recursive(node.right, ordered_search)

        return ordered_search

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        p_search = self.dfs_recursive(p, [])
        q_search = self.dfs_recursive(q, [])

        if p_search == q_search:
            return True
        else:
            print(str(p_search), str(q_search))
            return False


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))

p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))

p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))

solution = Solution()
# print(solution.dfs_recursive(root, []))

# assert solution.isSameTree(p1, q1), "Test Case Failed"
# print("Test Case Passed")

# assert not solution.isSameTree(p2, q2), "Test Case Failed"
# print("Test Case Passed")

# assert not solution.isSameTree(p3, q3), "Test Case Failed"
# print("Test Case Passed")

print(solution.isSameTree(p2, q2))
