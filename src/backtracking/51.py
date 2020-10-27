class Solution(object):
    def solveNQueens(self, n):
        def check(path):
            dif = 0
            for i in range(len(path)-2, -1, -1): #iterate the path backwards & check if the last element satisfy
                dif+=1
                #in order: check upperleft, upperright and column
                if path[-1] == path[i] + dif or path[-1] == path[i] - dif or path[-1] == path[i]:
                    return False
            return True
        
            
        def newLine(pos):
            arr = ['.' for _ in range(n)]
            arr[pos] = 'Q'
            return ''.join(arr)
        
        def nQueensHelper(path):
            if not check(path): #backtrack if path does not satisfy all conditions
                return
            if len(path) == n: #if path is complete and satisfies all conditions
                matches.append(path[:])
                return
            
            for i in range(n):
                if (not len(path) or i != path[-1]): #avoid adding the same number as the one right before that
                    path.append(i)
                    nQueensHelper(path) #path now is a list of numbers
                    path.pop()
        
        matches = []
        nQueensHelper([]) #populate matches with solutions
        result = []
        
        #transform to the format of output
        for match in matches:
            formattedMatch = []
            for idx in match:
                formattedMatch.append(newLine(idx))
            result.append(formattedMatch)
        return result
        
