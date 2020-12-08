class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict_t = collections.defaultdict(int)
        count = 0
        for num in nums:
            if dict_t[k-num] > 0:
                dict_t[k-num] -= 1
                count += 1
            else:
                dict_t[num] += 1
        return count
