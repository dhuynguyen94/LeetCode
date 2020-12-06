# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, None, None)

    def dfs(self, root, p, gp):
        if root is None:
            return 0
        if p and gp and gp.val % 2 == 0:
            return root.val + self.dfs(root.left, root, p) + self.dfs(root.right, root, p)
        return self.dfs(root.left, root, p) + self.dfs(root.right, root, p)


