class Solution:
    def uniquePaths(self, grid):
        MOD = 1000000007
        n = len(grid[0])

        dp = [[0, 0] for _ in range(n + 1)]

        # Starting point
        dp[1] = [1, 1]

        for row in grid:
            for j in range(n):

                if row[j] == 1:
                    # Mirror
                    dp[j + 1] = [
                        dp[j + 1][1],
                        dp[j][0]
                    ]

                else:
                    # Normal cell
                    ways = (dp[j][0] + dp[j + 1][1]) % MOD

                    dp[j + 1] = [ways, ways]

        return dp[n][0]