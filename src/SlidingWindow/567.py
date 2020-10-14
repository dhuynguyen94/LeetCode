import collections
def checkInclusion(self, s1: str, s2: str) -> bool:
    seen1 = collections.Counter(s1)
    seen2 = {}
    n1 = len(s1)
    start = 0
    for end, ch in enumerate(s2):
        if ch not in seen2:
            seen2[ch] = 1
        else:
            seen2[ch] += 1
        while end-start+1 >= n1:
            if end-start+1 == n1:
                if seen1 == seen2:
                    return True
            seen2[s2[start]] -= 1
            if seen2[s2[start]] == 0:
                seen2.pop(s2[start])
            start += 1
    return False


# Use 2 dictionaries to keep track of character counter for s1 and s2
# Slide window for fixed size of length s1.

# Time Complexity: O(n)
# Space Complexity: O(n)