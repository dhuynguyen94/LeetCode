class Solution(object):
    def dfs(self, courseDict, i, visited):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for course in courseDict[i]:
            if not self.dfs(courseDict, course, visited):
                return False

        visited[i] = 1
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [0] * numCourses
        courseDict = collections.defaultdict(list)
        for course in prerequisites:
            courseDict[course[1]].append(course[0])
        print(courseDict)
        for i in range(numCourses):
            if (self.dfs(courseDict, i, visited) == False):
                return False
        return True
