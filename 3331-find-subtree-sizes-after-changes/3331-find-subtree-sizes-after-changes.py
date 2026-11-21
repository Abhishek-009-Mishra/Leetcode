class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        self.adj = [[] for _ in range(n)]
        self.last = [-1] * 26
        self.ans = [0] * n

        # Build original tree
        for i in range(1, n):
            self.adj[parent[i]].append(i)

        newParent = parent[:]

        # Find new parents
        self.findParent(0, s, newParent)

        # Build modified tree
        self.adj = [[] for _ in range(n)]

        for i in range(1, n):
            self.adj[newParent[i]].append(i)

        # Choose either DFS or BFS
        self.dfs(0)

        # For BFS, use:
        # self.bfs(0, newParent)

        return self.ans

    def findParent(self, node, s, newParent):
        ch = ord(s[node]) - ord('a')
        old = self.last[ch]

        if old != -1:
            newParent[node] = old

        self.last[ch] = node

        for child in self.adj[node]:
            self.findParent(child, s, newParent)

        self.last[ch] = old

    # Method 1: DFS
    def dfs(self, node):
        size = 1

        for child in self.adj[node]:
            size += self.dfs(child)

        self.ans[node] = size
        return size

    # Method 2: BFS
    def bfs(self, root, newParent):
        from collections import deque

        n = len(self.adj)
        self.ans = [1] * n

        q = deque([root])
        order = []

        while q:
            node = q.popleft()
            order.append(node)

            for child in self.adj[node]:
                q.append(child)

        # Process nodes bottom-up
        for i in range(len(order) - 1, 0, -1):
            node = order[i]
            self.ans[newParent[node]] += self.ans[node]