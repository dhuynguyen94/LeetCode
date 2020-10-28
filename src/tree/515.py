class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dict = {}
        self.dfs(root, 0)
        return self.dict.values()

    def dfs(self, root, level):
        if root is None:
            return
        if level in self.dict:
            self.dict[level] = max(root.val, self.dict[level])
        else:
            self.dict[level] = root.val
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
