class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dict_t = collections.Counter(barcodes)
        heap, ans = [], []
        for key, freq in dict_t.items():
            heapq.heappush(heap, (-freq, key))
        while(heap):
            freq1, num1 = heapq.heappop(heap)
            ans.append(num1)
            if len(heap) >=1:
                freq2, num2 = heapq.heappop(heap)
                ans.append(num2)
                if freq2 + 1 < 0:
                    heapq.heappush(heap, (freq2+1, num2))
            
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1+1, num1))
                
        return ans
