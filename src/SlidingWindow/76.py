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
