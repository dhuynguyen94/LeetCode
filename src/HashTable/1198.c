class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        dict_t = collections.defaultdict(int)
        for row in mat:
            for num in row:
                dict_t[num] += 1
        ans = float('inf')
        for key in dict_t:
            if dict_t[key] == len(mat) and key < ans:
                ans = key
        if ans != float('inf'): return ans
        return -1
