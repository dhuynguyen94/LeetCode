# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        count1 = []
        count2 = []
        self.dfs(root1, count1)
        self.dfs(root2, count2)
        if len(count1) != len(count2):
            return False
        for i in range(len(count1)):
            if count1[i] != count2[i]:
                return False
        return True

    def dfs(self, root, count):
        # Base case
        if root is None:
            return
        # Do something
        if root.left is None and root.right is None:
            count.append(root.val)

        self.dfs(root.left, count)
        self.dfs(root.right, count)

