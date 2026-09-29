class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        isgood = cache(lambda i,j,d,m1,n1:
            False if (d:= d + (grid[i][j]=='(') - (grid[i][j]==')')) < 0  else
            True  if  d ==0 and i==m1 and j==n1  else
            (i<m1 and isgood(i+1,j,d,m1,n1)) or (j<n1 and isgood(i,j+1,d,m1,n1))
        )
        return  isgood(0,0,0, len(grid)-1, len(grid[0])-1)
        