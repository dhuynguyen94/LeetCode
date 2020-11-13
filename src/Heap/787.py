class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # Build graph
        graph = collections.defaultdict(list)
        for origin, destination, cost in flights:
            graph[origin].append((destination, cost))

        # (cost to src, # of stop to src, destination)
        heap = [(0, -1, src)]
        while heap:
            cost, stop, cur = heapq.heappop(heap)
            if stop > K:
                continue
            if cur == dst:
                return cost
            for neighbor, weight in graph[cur]:
                heapq.heappush(heap, (cost+weight, stop + 1, neighbor))

        return -1
