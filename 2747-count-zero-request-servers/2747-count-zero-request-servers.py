class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        logs.sort(key = lambda l: l[1])
        seen = {}                 # server -> requests in window
        ans = [0] * len(queries)
        i = j = 0                 # i = window start, j = window end

        for k in sorted(range(len(queries)), key = lambda k: queries[k]):
            q = queries[k]

            while j < len(logs) and logs[j][1] <= q:   # add new logs
                s = logs[j][0]
                seen[s] = seen.get(s, 0) + 1
                j += 1

            while i < j and logs[i][1] < q - x:       # drop old logs
                s = logs[i][0]
                seen[s] -= 1
                if seen[s] == 0:
                    del seen[s]
                i += 1

            ans[k] = n - len(seen)

        return ans
   