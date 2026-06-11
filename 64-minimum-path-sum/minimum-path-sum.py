class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        dp=[[0 for _ in range(c)]for _ in range(r)]
        s=0
        for i in range(c):
            s+=grid[0][i]
            dp[0][i]=s
        si=0
        for i in range(r):
            si+=grid[i][0]
            dp[i][0]=si
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j]=min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
        return dp[r-1][c-1]
