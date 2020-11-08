class Solution:
    # O(L^2 * N) T,S 
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        templates = {}
        graph = collections.defaultdict(list);
        
        # group words into templates
        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + '_' + word[i+1:]
                
                if template in templates:
                    templates[template].append(word)
                else:
                    templates[template] = [word]
                
        # build graph
        for temp in templates.keys():
            for word1 in templates[temp]:
                for word2 in templates[temp]:
                    if word1 != word2:
                        graph[word1].append(word2)
        
        # bfs
        visited = set()
        queue = collections.deque()
        queue.append((beginWord, 1))
        level = 1
        
        visited.add(beginWord)
        while queue:
            cur, level = queue.popleft()
            for word in graph[cur]:
                if word == endWord:
                    return level+1
                
                if word not in visited:
                    queue.append((word, level+1))
                    visited.add(word)
                    
        return 0
