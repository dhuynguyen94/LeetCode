class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        ans = 0
        for c in counter:
            ans += counter[c] % 2
        return ans <= 1

