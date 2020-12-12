class Solution(object):
    def maximalNetworkRank(self, n, roads):
        max_t = 0
        indegree = [0] * (n+1)
        mark = [[0 for _ in range(n+1)] for _ in range(n+1)] # Mark 2 node connected
        for a,b in roads:
            indegree[a] += 1
            indegree[b] += 1
            mark[a][b] = mark[b][a] = 1
        for i in range(len(indegree)-1):
            for j in range(i+1, len(indegree)):
                d = indegree[i] + indegree[j]
                if mark[i][j] or mark[j][i]:
                    d -= 1
                if d >= max_t:
                    max_t = d
        return max_t
