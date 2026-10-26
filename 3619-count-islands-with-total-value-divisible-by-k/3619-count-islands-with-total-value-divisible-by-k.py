class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        def dfs(row, col):
            visited[row][col] = True
            total = grid[row][col]

            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (0 <= nr < m and 0 <= nc < n
                        and grid[nr][nc] != 0
                        and not visited[nr][nc]):
                    total += dfs(nr, nc)+1

            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and not visited[i][j]:
                    island = dfs(i, j)
                    if island % k == 0:
                        count += 1

        return count