class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)] # dp[i] i번째에 도달 할 수 있는 방법
        dp[0] = 1
        dp[1] = 1
        
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
            
        
    

                

        