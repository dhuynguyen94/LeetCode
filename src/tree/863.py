# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)
        self.dfs1(root, graph)
        self.ans = []
        visited = set()
        self.dfs2(graph, target, visited, 0, K)
        return self.ans

    def dfs1(self, root, graph):
        if not root:
            return
        if root.left:
            graph[root].append(root.left)
            graph[root.left].append(root)
            self.dfs1(root.left, graph)
        if root.right:
            graph[root].append(root.right)
            graph[root.right].append(root)
            self.dfs1(root.right, graph)

    def dfs2(self, graph, src, visited, k, K):
        if k < K:
            if not src in visited:
                visited.add(src)
                for nei in graph[src]:
                    if not nei in visited:
                        self.dfs2(graph, nei, visited, k+1, K)
        else:
            self.ans.append(src.val)


