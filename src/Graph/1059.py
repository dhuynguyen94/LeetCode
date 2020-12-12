class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        visited = [0 for _ in range(n)]
        return self.dfs(graph, source, destination, visited)


    def dfs(self, graph, src, dst, visited):
        if len(graph[src]) == 0:
            return src == dst
        # detect cycle
        if visited[src] == -1:
            return False
        if visited[src] == 1:
            return True
        visited[src] = -1
        for neighbor in graph[src]:
            if not self.dfs(graph, neighbor, dst, visited):
                return False

        visited[src] = 1
        return True
