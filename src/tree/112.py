# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res = []
        self.dfs(root, sum, res)
        if len(res):
            return True
        return False

    def dfs(self, root, target, res):
        if not root:
            return
        if not root.left and not root.right and root.val == target:
            res.append(True)

        self.dfs(root.left, target-root.val, res)
        self.dfs(root.right, target-root.val, res)
