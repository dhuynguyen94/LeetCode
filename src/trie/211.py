class TrieNode:
    def __init__(self, word):
        self.word = word
        self.child = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        parent = self.root
        for i, c in enumerate(word):
            if not c in parent.child:
                parent.child[c] = TrieNode(word)
            parent = parent.child[c]
            if i == len(word)-1:
                parent.end = True

    def dfs (self, parent, word):
        if not word:
            if parent.end:
                self.res = True
            return
        elif word[0] == '.':
            for child in parent.child.values():
                self.dfs(child, word[1:])
        else:
            child = parent.child.get(word[0])
            if not child:
                return
            self.dfs(child, word[1:])
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.res = False
        self.dfs(self.root, word)
        return self.res
