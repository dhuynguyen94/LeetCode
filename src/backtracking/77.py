class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.backtracking(n+1, k, [], 1)
        return self.ans

    def backtracking(self, n, k, path, idx):
        if len(path) == k:
            self.ans.append(path[:])
            return

        for i in range(idx, n):
            path.append(i)
            self.backtracking(n, k, path, i+1)
            path.pop()

