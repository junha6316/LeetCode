class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        dp[i][j] = min(dp[i-1][j], dp[i-1][j]) + nums[i][j]
        """
        dp = [[0 for i in range(len(row))] for row in triangle]
        # initialize
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dp[i][0] = triangle[i][0] + dp[i-1][0]
            dp[i][-1] = triangle[i][-1] + dp[i-1][-1]
            
        for i in range(1, len(triangle)):
            row = triangle[i]
            for j in range(1, len(row)-1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

            
            
        return min(dp[-1])
        
            
        