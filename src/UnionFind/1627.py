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
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n+1)
        for i in range(1, n+1):
            for j in range(2*i, n+1, i):
                if i > threshold:
                    uf.union(i,j)
        ans = []
        for query in queries:
            root_x = uf.find(query[0])
            root_y = uf.find(query[1])
            ans.append(root_x == root_y)
        return ans


