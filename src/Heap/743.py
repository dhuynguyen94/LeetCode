class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for src, dest, w in times:
            graph[src].append((dest, w))
        heap = [(0, K)]
        visited = {}
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited[node] = dist
            for nei, new_dist in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (dist + new_dist, nei))
        return max(visited.values()) if len(visited) == N else -1
