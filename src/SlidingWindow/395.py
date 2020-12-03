class Solution:
    #Since we cannot know what is the condition to shrink the sliding windows,
    #we must try all the possibilities of having from 1 to 26 unique characters in the windows
    #When number of unique char in the windows > the target Unique number, we shrink the windows
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        C = Counter(s)
        for iteration in range(1, len(C)+1):
            res = max(res, self.helper(s, k, iteration))
        return res
    
    def helper(self, s, k, targetUnique):
        i = countAtLeastK = 0
        hmap = {}
        res = 0
        countUnique = 0
        for j in range(0, len(s)):
            #Update counter
            hmap[s[j]] = hmap.get(s[j],0) + 1
            if hmap[s[j]] == 1:
                countUnique += 1
            #must be equal, since each unique character can only contribute to countAtLeastK one time
            if hmap[s[j]] == k: 
                countAtLeastK += 1
            
            #Make it valid
            while countUnique > targetUnique:
                if hmap[s[i]] == k:
                    countAtLeastK -= 1
                hmap[s[i]] -= 1
                if hmap[s[i]] == 0:
                    countUnique -= 1
                i += 1
            if countAtLeastK == countUnique:
                res = max(res, j - i + 1) 
        return res