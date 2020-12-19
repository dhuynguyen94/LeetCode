# Union find without rank
class UnionFind:
    def __init__(self, n):
        self.uf = []
        for i in range(n):
            self.uf.append(i)
    def find(self, x):
        if self.uf[x] == x:
            return x
        return self.find(self.uf[x])
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.uf[root_x] = root_y
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = UnionFind(len(edges))
        for edge in edges:
            if not ds.union(edge[0]-1, edge[1]-1):
                return edge
        return None

# Union find with rank
class UnionFind:
    def __init__(self, n):
        self.uf = []
        self.rank = [0] * n
        for i in range(n):
            self.uf.append(i)
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = UnionFind(len(edges))
        for edge in edges:
            if not ds.union(edge[0]-1, edge[1]-1):
                return edge
        return None
