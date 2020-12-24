class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for c in counter:
            pairs = counter[c] // 2
            ans += 2*pairs
        if ans < len(s): ans += 1
        return ans

