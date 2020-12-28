class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_t = Counter(nums1)
        ans = []
        for num in nums2:
            if num in dict_t and dict_t[num] > 0:
                ans.append(num)
                dict_t[num] -= 1
        return ans

