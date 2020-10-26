class TrieNode:
    def __init__(self, val):
        self.child = {}
        self.end = False
        self.val = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(0)


    def insert(self, key: str, val: int) -> None:
        parent = self.root
        for c in key:
            if not c in parent.child:
                parent.child[c] = TrieNode(0)
            parent = parent.child[c]
        parent.end = True
        parent.val = val


    def dfs(self, root, val):
        if root.val != 0:
            val[0] += root.val
        for c in root.child:
            self.dfs(root.child[c], val)
    def sum(self, prefix: str) -> int:
        parent = self.root
        for c in prefix:
            if not c in parent.child:
                return 0
            parent = parent.child[c]
        val = [0]
        self.dfs(parent, val)
        return val[0]

