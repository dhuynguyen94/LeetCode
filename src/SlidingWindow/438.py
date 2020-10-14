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
    