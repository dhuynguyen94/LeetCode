class Solution:
    def countVowelStrings(self, n: int) -> int:
        s = 'aeiou'
        self.ans = 0
        self.backtracking(s, n, [], 0)
        return self.ans

    def backtracking(self, s, n, path, idx):
        if len(path) == n:
            self.ans += 1
            return

        for i in range(idx, len(s)):
            path.append(s[i])
            self.backtracking(s, n, path, i)
            path.pop()

