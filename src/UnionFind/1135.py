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
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        ans = 0
        ds = UnionFind(N)
        connections.sort(key = lambda x: x[2])
        for conn in connections:
            if ds.union(conn[0]-1, conn[1]-1):
                ans += conn[2]
        # Check all nodes connect together
        check = ds.find(0)
        for i in range(N):
            if ds.find(i-1) != check:
                return -1
        return ans

