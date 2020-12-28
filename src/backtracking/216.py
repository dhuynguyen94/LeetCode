class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.backtracking(n, k , [], 1)
        return self.ans
    def backtracking(self, n, k, path, idx):
        if len(path) == k and n == 0:
            self.ans.append(path[:])
            return
        if n < 0:
            return

        for i in range(idx, 10):
            path.append(i)
            self.backtracking(n-i, k, path, i+1)
            path.pop()
