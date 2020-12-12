class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for i in range(len(rooms)):
            if i == rooms[i]:
                return False
            graph[i] = rooms[i]

        visited = set()
        self.dfs(graph, 0, visited)
        return len(visited) == len(rooms)

    def dfs(self, graph, src, visited):
        visited.add(src)
        for neighbor in graph[src]:
            if not neighbor in visited:
                self.dfs(graph, neighbor, visited)

