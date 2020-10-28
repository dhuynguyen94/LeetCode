class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.dict = {}
        return self.dfs(root, 0)


    def dfs(self, root, level):
        if not root:
            return True
        if level % 2 == 0 and root.val % 2 == 0: # Check node is even, and level is even
            return False
        if level % 2 == 1 and root.val % 2 == 1: # Check node is odd, and level is odd
            return False
        if not level in self.dict:
            self.dict[level] = [root.val]
        else:
            if level % 2 == 0:
                if root.val <= self.dict[level][-1]:  # Check sort for even level
                    return False
            else:
                if root.val >= self.dict[level][-1]:  # Check sort for odd level
                    return False
            self.dict[level].append(root.val)

        return self.dfs(root.left, level + 1) and self.dfs(root.right, level + 1)
