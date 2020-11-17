def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    start = 0
    result = 0
        
    for end, char in enumerate(s):
        if char not in seen:
            result =max(result, end-start+1)
        else:
            if seen[char] < start:
                result =max(result, end-start+1)
            else:
                start = seen[char] + 1
        seen[char] = end
    return result    

    #Use hashmap to store the last index each char was seen. 
    # Time Complexity: O(n)
    # Space Complexity: O(n)

#Second solution, following template
def lengthOfLongestSubstring2(s: str) -> int:
    hset = set()
    i,res = 0,0
    for j in range(0, len(s)):
        while s[j] in hset:
            hset.remove(s[i])
            i += 1
        hset.add(s[j])
        res = max(res, j - i + 1)
    return res