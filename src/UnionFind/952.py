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
    def largestComponentSize(self, A: List[int]) -> int:
        max_t = max(A)
        uf = UnionFind(max_t+1)

        for num in A:
            for factor in range(2, int(sqrt(num))+ 1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)
        group = defaultdict(int)
        ans = 0
        for num in A:
            root = uf.find(num)
            group[root] += 1
            ans = max(ans, group[root])

        return ans
