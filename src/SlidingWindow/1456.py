class Solution(object):
    def maxVowels(self, s, k):
        if k == 0: return 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        n = len(s)
        count = 0
        for i in range(k):
            if s[i] in vowel:
                count += 1
        ans = count
        for i in range(n - k):
            if s[i] in vowel:
                count -= 1
            if s[i + k] in vowel:
                count += 1
            ans = max(ans, count)
        return ans
