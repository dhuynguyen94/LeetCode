class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0
        self.backtrack(n,0,set(),[],0)

        print(self.result)
        return self.result
    
    def backtrack(self, n, row, invalid_pos, curr_pos, result):
        if row == n:
            self.result += 1
            return
            
        for i in range(row,n):
            for j in range(n):
                pos = (i,j)
                if pos in invalid_pos:
                    continue
                # print(pos)
                curr_pos.append(pos)
                pre_invalid_pos = invalid_pos
                invalid_pos = invalid_pos | self.compute_invalid_pos(pos,n)
                self.backtrack(n,row+1,invalid_pos,curr_pos,result)
                # print(result)
                curr_pos.pop()
                invalid_pos = pre_invalid_pos
            return
        # return result
                
            
    
    def compute_invalid_pos(self, pos,n):
        result = set()
        i = pos[0]
        left = self.compute_left(pos,n)
        right = self.compute_right(pos,n)
        mid = self.compute_mid(pos,n)
        result = result | left | mid | right      
        # print(left|mid | right)
        return result
    
    def compute_left(self,pos,n):
        result = set()
        row = pos[0] + 1
        for i in range(pos[1]-1,-1,-1):
            if row >= n:
                break
            result.add((row,i))
            row = row + 1            
        return result 
    
    def compute_mid(self,pos,n):
        result = set()
        for i in range(pos[0]+1,n):
            result.add((i,pos[1]))
        return result 
    
    def compute_right(self,pos,n):
        result = set()
        row = pos[0] + 1
        for i in range(pos[1]+1,n):
            if row >= n:
                break
            result.add((row,i))
            row = row + 1            
        return result       