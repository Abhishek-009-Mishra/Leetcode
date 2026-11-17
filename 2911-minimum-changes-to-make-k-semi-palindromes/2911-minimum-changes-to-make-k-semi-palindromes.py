class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        divisors = [[] for _ in range(n + 1)]

        for d in range(1, n + 1):
            for v in range(1, d):
                if d % v == 0:
                    divisors[d].append(v)

        cost = [[INF] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF

                for d in divisors[L]:
                    changes = 0

                    for start in range(i, i + d):
                        l = start
                        r = start + ((j - start) // d) * d

                        while l < r:
                            if s[l] != s[r]:
                                changes += 1

                            l += d
                            r -= d

                    best = min(best, changes)

                cost[i][j] = best

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for t in range(1, k + 1):
            for i in range(t, n + 1):
                for j in range(t - 1, i):
                    if dp[t - 1][j] < INF and cost[j][i - 1] < INF:
                        dp[t][i] = min(
                            dp[t][i],
                            dp[t - 1][j] + cost[j][i - 1]
                        )

        return dp[k][n]