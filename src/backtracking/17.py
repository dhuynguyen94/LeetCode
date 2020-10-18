   dialPad = {"2":'abc',
                   "3": 'def',
                   "4": 'ghi',
                   "5": 'jkl',
                   "6": 'mno',
                   "7": 'pqrs',
                   "8": 'tuv',
                   "9": 'wxyz'}
 # backtrack
        result = []
        if len(digits) == 0:
            return
        self.backtrackletterCombinations(dialPad,result,digits,[],0)
        return result
    def backtrackletterCombinations(self,dialPad,result,digits,path,index):
        if index == len(digits):
            result.append(''.join(path[:]))
            return 
        for i in range(len(dialPad[digits[index]])):
            path.append(dialPad[digits[index]][i])
            self.backtrackletterCombinations(dialPad,result,digits,path,index+1)
            path.pop()     
      
      
      
 # recursive
        # base case
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return dialPad[digits[0]]
        
        
        
        # recursive function     #234
        first_number = dialPad[digits[0]] #2 #3
        second_number = self.letterCombinations(digits[1:]) # recursive #34  #4 
        result = []
        for item1 in first_number: #2   #3
            for item2 in second_number: #34 #4
                result.append(item1 + item2)  #2 + #34
        return result
