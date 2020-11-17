class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = collections.defaultdict(int)
        j, ans = 0,0
        for i in range(len(s)):
            counter[s[i]] += 1
            while len(counter) > 2:    # Shrink the Window
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    del counter[s[j]]
                j += 1
            ans = max(ans, i - j + 1)
        return ans
