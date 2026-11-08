class Solution:
    def countServers(self, A):
        x, y = tuple(map(sum, A)), tuple(map(sum, zip(*A)))
        return sum(x[i] + y[j] > 2 for i in range(len(A)) for j in range(len(A[0])) if A[i][j])