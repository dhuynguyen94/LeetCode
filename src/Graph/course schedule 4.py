def checkIfPrerequisite(n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
    rel = collections.defaultdict(list)
    visited = [0] * n
    for p in prerequisites:
        rel[p[0]].append(p[1])
            
    res = []
        
    for pair in queries:
        start = pair[0]
        end = pair[1]
        if end in rel[start]:
            res.append(True)
        else:
            v = bfs(start, end, rel)
            res.append(v)
    return res
            

            
            
def bfs(start, end, rel):
    q = collections.deque()
    q.append(start)
    visited = set()
    visited.add(start)
    while q:
        cur = q.popleft()
        if cur == end:
            return True
        for node in rel[cur]:
            if node not in visited:
                visited.add(node)
                q.append(node)
    return False