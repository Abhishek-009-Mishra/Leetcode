class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] == 1:
                return

            grid[r][c] = 1

            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # Remove land touching the boundary
        # First & Last columns
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # First & Last rows
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Count remaining closed islands
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    ans += 1
                    dfs(r, c)

        return ans