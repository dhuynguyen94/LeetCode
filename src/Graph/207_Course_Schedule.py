def canFinish(numCourses, prerequisites):
    courseDict = collections.defaultdict(list)
    visited = [0] * numCourses
    for p in prerequisites:
        cur_class = p[0]
        preq_class = p[1]
        courseDict[cur_class].append(preq_class)
        
    for course in range(numCourses): 
        #DFS -> detect cycle -> returns False if cycle exists, else True
        if dfs(course, courseDict, visited) == False:
            return False
    return True

def dfs(course, courseDict, visited):
    if visited[course] == -1:
        return False
    #If we have already been through, and there is no cycle
    if visited[course] == 1:
        return True
        # Mark -1 for processing node
    visited[course] = -1
        
    for neighbor in courseDict[course]:
        if dfs(neighbor, courseDict, visited) == False:
            return False
    visited[course] = 1
    return True