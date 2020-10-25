Problem explanation:
# A knows B, B knows A -> direct friend
# B knows C, C knows B -> B, C is direct friend, A, C is indirect friend
        
# Friend circle: has mutual friend or is friend ... means is directed friend or indirected friend. 


def findCircleNum(related: List[List[int]]) -> int:
    n = len(related)
    group = 0
    visited = [False for _ in range(n)]
        
    # adjList = collections.defaultdict(list)
        
    #Construct graph
    for i in range(n):
        for j in range(n):
            if related[i][j] == 1:
                adjList[i].append(j)
    
    # DFS or BFS
    for i in range(n):
        if i not in viisted:
            dfs(visited,related, i) # or call bfs function instead
            group += 1
    return group  

def dfs(visited, related, i):
    for j in range(len(related)):
        if related[i][j] == 1 and j not in visited:
            visited.add(j)
            dfs(visited, related, j)

def bfs(adjList, visited, q, i): # Use adj list instead of related
    visited.add(i)
    q.append(i)
    while q:
        cur = q.popleft()
        for neighbor in adjList[cur]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


# Complexity: O(n^2)
# Space : O(n)

