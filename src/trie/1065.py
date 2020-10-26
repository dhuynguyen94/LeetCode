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

    def search(self, word):
        parent = self.root
        for c in word:
            if not c in parent.child:
                return False
            parent = parent.child[c]
        return parent.end

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        graph = Trie()
        for word in words:
            graph.insert(word)

        ans = []
        for i in range(len(text)):
            for j in range(i, len(text)):
                if graph.search(text[i:j+1]):
                    ans.append([i, j])
        return ans
