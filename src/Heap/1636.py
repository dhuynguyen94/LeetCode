class Num:
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.num > other.num
        return self.freq < other.freq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict_t = collections.Counter(nums)
        heap, ans = [], []
        for key,freq in dict_t.items():
            heapq.heappush(heap, Num(key,freq))
        while len(heap):
            val = heapq.heappop(heap)
            for i in range(val.freq):
                ans.append(val.num)
        return ans
