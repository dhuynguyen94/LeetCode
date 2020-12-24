class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_t = collections.defaultdict(int)
        j, ans = 0, 0
        for i in range(len(s)):
            dict_t[s[i]] += 1
            while i - j + 1 - max(dict_t.values()) > k:  # Shrink window
                dict_t[s[j]] -= 1
                j += 1
            ans = max(ans, i - j + 1)
        return ans

