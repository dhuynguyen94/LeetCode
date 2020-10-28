class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        ans = []
        node_dict = {}
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop()
            if node:
                if not level in node_dict:
                    node_dict[level] = [node.val]
                else:
                    node_dict[level].append(node.val)

                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))

        for key in node_dict.keys():
            if key % 2 != 0:
                ans.append(node_dict[key][::-1])
            else:
                ans.append(node_dict[key])
        return ans
        """
        ans = []
        self.dict_t = collections.defaultdict(list)
        self.dfs(root, 0)
        for key in self.dict_t:
            if key % 2 != 0:
                ans.append(self.dict_t[key][::-1])
            else:
                ans.append(self.dict_t[key])
        return ans

    def dfs(self, root, level):
        if root is None:
            return
        self.dict_t[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
