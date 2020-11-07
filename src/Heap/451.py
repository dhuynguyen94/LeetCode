class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_dict = {}
        ans = ""
        for char in s:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        for key, val in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
            for i in range(val):
                ans += key
        return ans


"""
        Using heapq
        dict_t = collections.Counter(s)
        heap = []
        ans = ''
        for key, val in dict_t.items():
            heapq.heappush(heap, (-val, key))
        while heap:
            freq, char = heapq.heappop(heap)
            for i in range(-freq):
                ans += char
        return ans
"""
