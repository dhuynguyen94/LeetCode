class Solution:
    def minDeletions(self, s: str) -> int:
        dict_t = collections.Counter(s)
        used = set()
        ans = 0
        for freq in dict_t.values():
            while freq in used and freq > 0:
                freq -= 1
                ans += 1
            used.add(freq)
        return ans
