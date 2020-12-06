# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        countSum = []
        self.dfs(root, sum, [], countSum)
        return countSum

    def dfs(self, root, sum, ls, countSum):
        if root is None:
            return
        if root.left is None and root.right is None and root.val == sum:
            ls.append(root.val)
            countSum.append(ls)

        self.dfs(root.left, sum - root.val, ls + [root.val], countSum)
        self.dfs(root.right, sum - root.val, ls + [root.val], countSum)

