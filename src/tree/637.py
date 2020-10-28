class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.dict = collections.defaultdict(list)
        self.dfs(root, 0)
        ans = []
        for key,val in sorted(self.dict.items()):
            average = float(sum(val)) / float(len(val))
            ans.append(average)
        return ans

    def dfs(self, root, level):
        if root is None:
            return
        self.dict[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
