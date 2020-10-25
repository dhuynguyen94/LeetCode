def dfs(courseDict, visited, i, order):       
    if visited[i] == -1:
        return False
    if visited[i] == 1:
        return True
    visited[i] = -1
    for n in courseDict[i]:
        if not dfs(courseDict, visited,n , order):
            return False
    visited[i] = 1
    order.append(i)
    return True
            
        
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    courseDict = collections.defaultdict(list)
    order = []
    visited = [0] * numCourses
    for p in prerequisites:
        courseDict[p[0]].append(p[1])
    for course in range(numCourses):
        if not dfs(courseDict, visited, course, order):
            return []   
    return order