class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        parent = self.root
        for c in word:
            if not c in parent.child:
                parent.child[c] = TrieNode()
            parent = parent.child[c]
        parent.end = True

    def check(self, word): # check camel case from a world
        parent = self.root
        for c in word:
            # Capital case not in dict
            if not c in parent.child and c.isupper():
                return False
            elif c in parent.child:
                parent = parent.child[c]
        return parent.end == True

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        trie = Trie()
        trie.insert(pattern) # Trie only contains capital case
        for querie in queries:
            if trie.check(querie):
                ans.append(True)
            else:
                ans.append(False)
        return ans

