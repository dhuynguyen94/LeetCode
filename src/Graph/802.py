class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dict_t = collections.defaultdict(list)
        for i in range(len(graph)):
            dict_t[i] = graph[i]
        ans = []
        visited = [0] *len(graph)
        for i in range(len(graph)):
            if self.dfs(dict_t, i, visited):
                ans.append(i)

        return ans

    def dfs(self, dict_t, node, visited):
        if len(dict_t[node]) == 0:
            return True
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True
        visited[node] = -1
        for neighbor in dict_t[node]:
            if not self.dfs(dict_t, neighbor, visited):
                return False

        visited[node] = 1
        return True
