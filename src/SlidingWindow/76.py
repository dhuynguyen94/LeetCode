class Solution(object):
    def minWindow(self, s, t):
        dict_t = Counter(t)
        state = Counter()
        i, j = 0, 0
        form = 0
        target = len(dict_t)
        ans = [float('inf'), None]
        while i < len(s):
            char = s[i]
            # Expand windows until reaching the target
            if char in dict_t:
                state[char] += 1
                if state[char] == dict_t[char]:
                    form += 1
            # Shrink the windows
            while j <= i and form == target:
                char = s[j]
                if i - j + 1 < ans[0]:  # Update the min size window
                    ans[0] = i - j + 1
                    ans[1] = j

                if char in dict_t:
                    state[char] -= 1
                    if state[char] == dict_t[char] -1:
                        form -= 1
                j += 1

            i += 1
        if ans[0] == 'inf' or ans[1] == None:
            return ""
        return s[ans[1]: ans[1]+ans[0]]
    
    #Another solution using one dictionary only
    def minWindow2(self, s: str, t: str) -> str:
        hmap = {}
        i, counter = 0,0
        res = [0,len(s)]
        for c in t:
            hmap[c] = hmap.get(c,0) + 1
        for j in range(0,len(s)):
            if s[j] in hmap:
                if hmap[s[j]] >= 1:
                    counter += 1
                hmap[s[j]] -= 1
            #when it is valid, increment i as much as we can
            while counter == len(t): 
                if j - i < res[1] - res[0]: #new minimum substring
                    res[0] = i
                    res[1] = j
                if s[i] in hmap:
                    hmap[s[i]] += 1
                    if hmap[s[i]] >= 1:
                        counter -= 1
                i += 1
        return "" if res[1] == len(s) else s[res[0]:res[1]+1]
