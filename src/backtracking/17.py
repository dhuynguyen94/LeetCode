class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0: return []
        self.ans = []
        self.backtrack(digits, [], 0)
        return self.ans

    def backtrack(self, digits, path, idx):
        if idx == len(digits):   # base case
            self.ans.append(''.join(path))
            return
        val_digit = self.phone[digits[idx]]
        for i in range(len(val_digit)):
            path.append(val_digit[i])
            self.backtrack(digits, path, idx+1)
            path.pop()
