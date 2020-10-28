class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dict_t = collections.defaultdict(int)
        self.dfs(root, dict_t, 1)
        max_value = float('-inf')
        for key in dict_t:
            if dict_t[key] > max_value:
                max_value = dict_t[key]
                max_key = key
        return max_key

    def dfs(self, root, dict_t, level):
        if root is None:
            return
        dict_t[level] += root.val
        self.dfs(root.left, dict_t, level + 1)
        self.dfs(root.right, dict_t, level + 1)
