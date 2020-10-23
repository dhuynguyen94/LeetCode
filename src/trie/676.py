class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        parent = self.root
        for c in word:
            if not c in parent.child:
                parent.child[c] = TrieNode()
            parent = parent.child[c]
        parent.end = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.addWord(word)

    def dfs(self, remain, root, searchWord):
        if not searchWord:
            if remain == 0 and root.end == True:
                self.res = True
            return

        for c in root.child:
            if c == searchWord[0]:
                self.dfs(remain, root.child[c], searchWord[1:])
            elif remain == 1:
                self.dfs(0, root.child[c], searchWord[1:])
    def search(self, searchWord: str) -> bool:
        self.res = False
        self.dfs(1, self.root, searchWord)
        return self.res

