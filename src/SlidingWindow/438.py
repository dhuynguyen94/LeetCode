import collections
def findAnagrams(self, s: str, p: str) -> List[int]:
    pSeen = collections.Counter(p)
    sSeen = {}
    start = 0
    nP = len(p)
    result = []

    for end, ch in enumerate(s):
        if ch not in sSeen:
            sSeen[ch] = 1
        else:
            sSeen[ch] += 1
        while end-start + 1 >= nP:
            if end-start+1 == nP and sSeen == pSeen:
                result.append(start)
            sSeen[s[start]] -= 1
            if sSeen[s[start]] == 0:
                sSeen.pop(s[start])
            start += 1
    return result


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        k = len(p)
        dict_p = collections.Counter(p)
        dict_s = collections.Counter(s[:len(p)])
        if dict_p == dict_s:
            ans.append(0)
        for i in range(k, len(s)):
            dict_s[s[i]] += 1
            dict_s[s[i-k]] -= 1
            if dict_s[s[i-k]] == 0:
                del dict_s[s[i-k]]
            if dict_s == dict_p:
                ans.append(i-k+1)
        return ans

#Another solution using one dictionary, and following the template

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        hmap = {}
        i = lenCounter = 0
        for c in p:
            hmap[c] = hmap.get(c,0) + 1
        res = []
        for j in range(0, len(s)):
            if s[j] in hmap:
                hmap[s[j]] -= 1
                if hmap[s[j]] >= 0:
                    lenCounter += 1
            if lenCounter == len(p):
                res.append(i)
            if j - i + 1 == len(p):
                if s[i] in hmap:
                    if hmap[s[i]] >= 0:
                        lenCounter -= 1
                    hmap[s[i]] += 1
                i += 1
        return res