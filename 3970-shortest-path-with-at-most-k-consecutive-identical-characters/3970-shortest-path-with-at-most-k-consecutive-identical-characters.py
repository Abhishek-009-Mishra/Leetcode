class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        INF = float("inf")
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        while pq:
            d, u, r = heapq.heappop(pq)
            if d > dist[u][r]:
                continue
            if u == n - 1:
                return d
            for v, w in adj[u]:
                nr = r + 1 if labels[v] == labels[u] else 1
                if nr > k:
                    continue
                if d + w < dist[v][nr]:
                    dist[v][nr] = d + w
                    heapq.heappush(pq, (d + w, v, nr))
        return -1