# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        ans, level = self.dfs(root, 0)
        return ans

    def dfs(self, root, level):
        if not root:
            return root, level

        left, left_level = self.dfs(root.left, level + 1)
        right, right_level = self.dfs(root.right, level + 1)

        if left_level == right_level:
            return root, left_level + 1
        elif left_level > right_level:
            return left, left_level + 1
        else:
            return right, right_level + 1
