class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
     
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
            else:
                break
                
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
            else:
                break
                
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] += dp[r-1][c] + dp[r][c-1]
            
        return dp[-1][-1]
        
        
        
                
        
                
            
                
        
        