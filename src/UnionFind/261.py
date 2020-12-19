class UnionFind:
    def __init__(self, n):
        self.uf = list(range(n))
        self.rank = [0] * n
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
        return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        ds = UnionFind(n)
        for edge in edges:
            if not ds.union(edge[0], edge[1]):
                return False
        return True

