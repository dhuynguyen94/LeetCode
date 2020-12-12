class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_t = {}
        for i in range(len(graph)):
            graph_t[i] = graph[i]
        self.ans = []
        self.dfs(graph_t, 0, [])
        return self.ans


    def dfs(self, graph_t, node, path):
        if node == 0:
            path.append(0)
        if node == len(graph_t) - 1:
            self.ans.append(path)
        for neighbor in graph_t[node]:
            self.dfs(graph_t, neighbor, path + [neighbor])
