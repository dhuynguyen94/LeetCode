class Solution:
    def reorganizeString(self, S: str) -> str:
        dict_t = collections.Counter(S)
        heap, ans = [], ''
        for key, freq in dict_t.items():
            heapq.heappush(heap, (-freq, key))
        while heap:
            if len(heap) >= 2:
                freq1, chr1 = heapq.heappop(heap)
                ans += chr1
                freq2, chr2 = heapq.heappop(heap)
                ans += chr2
                if freq1 + 1 < 0:
                    heapq.heappush(heap, (freq1+1, chr1))
                if freq2 + 1 < 0:
                    heapq.heappush(heap, (freq2+1, chr2))
            else:
                freq1, chr1 = heapq.heappop(heap)
                ans += chr1
                if freq1 + 1 != 0:
                    return ''
        return ans
