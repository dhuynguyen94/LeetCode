class TrieNode:
    def __init__(self):
        self.word = ''
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
        parent.word = word

    def bfs(self):
        res = ''
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            for child in node.child.values():
                if child.end:
                    queue.append(child)
                    if len(child.word) > len(res) or child.word < res:
                        res =  child.word
        return res



class Solution:
    def longestWord(self, words: List[str]) -> str:
        graph = Trie()
        for word in words:
            graph.insert(word)
        return graph.bfs()
