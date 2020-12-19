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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n > len(connections) + 1:
            return -1
        ds = UnionFind(n)
        count = n
        for conn in connections:
            if ds.union(conn[0], conn[1]):
                count -= 1
        return count - 1
