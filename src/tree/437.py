# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):

        self.path = 0
        self.dfs_all_root(root, sum)
        return self.path


    def dfs_all_root(self, root, sum_t):
        if root is None:
            return

        # do something
        self.dfs(root, sum_t)
        self.dfs_all_root(root.left, sum_t)
        self.dfs_all_root(root.right, sum_t)


    def dfs(self, root, sum_t):
        if root is None:
            return

        if root.val == sum_t:
            self.path += 1

        self.dfs(root.left, sum_t-root.val)
        self.dfs(root.right, sum_t-root.val)

