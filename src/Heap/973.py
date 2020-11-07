import math
import heapq
class Point:
    def __init__(self, point):
        self.point = point
        self.distance = math.sqrt(pow(point[0],2) + pow(point[1], 2))

    def __eq__(self, other):
        return self.distance == other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance
class Solution(object):

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        heapq.heapify(heap)
        for point in points:
            heapq.heappush(heap, Point(point))

        ret = []
        count = 0
        for _ in range(len(heap)):
            if count == K:
                return ret
            ret.append(heapq.heappop(heap).point)
            count += 1
        return ret


