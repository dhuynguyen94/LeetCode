
def countComponents(n, edges):
    #1. Build graph
    graph = collections.defaultdict(list)
    visited = set()
        
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    cnt = 0

    for i in range(n):
        if i not in visited:
            dfs(graph, i, visited)
            cnt += 1
    return cnt
    
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(adjList, node, visited):
    queue = collections.deque()
    # put the first node into queue
    queue.append(node)
    while queue:
        # Pop queue
        n = queue.popleft()
        # Look neighbor
        for neighbor in adjList[n]:
            if not neighbor in visited:
                # Add back to the queue
                visited.add(neighbor)
                queue.append(neighbor)


# Complexity: O(n)
# Time Complexity O(n)