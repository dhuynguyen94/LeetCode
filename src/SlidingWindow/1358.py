# Time Complexity: O(n)
# Space Complexity: O(1)
# HashMap solution
def numberOfSubstrings(self, s: str) -> int:
    hmap = {}
    i = 0
    res = 0
    for j in range(0, len(s)):
        hmap[s[j]] = hmap.get(s[j],0) + 1
        while ( 'a' in hmap and 'b' in hmap and 'c' in hmap and hmap['a'] > 0 and hmap['b'] > 0 and hmap['c'] > 0):
            #if the subtring from i to j is valid, then all the subtring from i to end is valid
            res += len(s) - j
            hmap[s[i]] -= 1
            i += 1
    return res

# Time Complexity: O(n)
# Space Complexity: O(1)
# Counter solution
def numberOfSubstrings2(self, s: str) -> int:
    #number of valid substrings from the position j : len(s) - j + 1
    i = 0
    ca, cb, cc = 0,0,0 #count of a,b,c
    res = 0 
    for j in range(0, len(s)):
        if s[j] == 'a':
            ca += 1
        if s[j] == 'b':
            cb += 1
        if s[j] == 'c':
            cc += 1
        while ( ca > 0 and cb > 0 and cc > 0 ):
            res += len(s) - j
            if s[i] == 'a':
                ca -= 1
            if s[i] == 'b':
                cb -= 1
            if s[i] == 'c':
                cc -= 1
            i += 1
    return res