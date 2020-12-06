# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        count = []
        self.dfs(root, "", count)
        return count

    def dfs(self, root, path, count):
        if root is None:
            return
        if root.left is None and root.right is None:
            path = path + str(root.val)
            count.append(path)
        self.dfs(root.left, path + str(root.val) +'->', count)
        self.dfs(root.right, path + str(root.val) + '->', count)
