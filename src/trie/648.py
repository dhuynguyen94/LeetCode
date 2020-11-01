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
        ans = ''
        for c in word:
            if not c in parent.child:
                return word
            ans += c
            parent = parent.child[c]
            if parent.end == True:
                return ans
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        graph = Trie()
        list_word = sentence.split()
        for dic in dictionary:
            graph.insert(dic)
        ans = []
        for word in list_word:
            ans.append(graph.search(word))

        return " ".join(ans)
