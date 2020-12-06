# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = []
        self.dfs(root, count)
        return count
    def dfs(self, root, count):
        if root is None:
            return
        if root.right is None and root.left:
            count.append(root.left.val)
        elif root.left is None and root.right:
            count.append(root.right.val)
        self.dfs(root.left, count)
        self.dfs(root.right, count)

