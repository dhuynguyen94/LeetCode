class UnionFind:
    def __init__(self, n):
        self.uf = list(range(n))
        self.rank = [0] * n
        self.count = n
    def find(self, x):
        if self.uf[x] == x:
            return x
        return self.find(self.uf[x])
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        # Always attach a smaller depth tree under the
        # root of the deeper tree.
        if self.rank[root_x] > self.rank[root_y]:
            self.uf[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.uf[root_x] = root_y
        else:
            self.uf[root_x] = root_y
            self.rank[root_y] += 1
        self.count -= 1
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        for parent, nodes in enumerate(zip(leftChild, rightChild)):
            left, right = nodes[0], nodes[1]
            if left != -1:
                if not uf.union(parent, left): return False
            if right != -1:
                if not uf.union(parent, right): return False

        return uf.count == 1
