class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        j, ans = 0, 0
        cost = 0
        for i in range(len(s)):
            cost += abs(ord(s[i]) - ord(t[i]))
            while cost > maxCost: #shrink Window
                cost -= abs(ord(s[j]) - ord(t[j]))
                j += 1
            ans = max(ans, i - j + 1)
        return ans
