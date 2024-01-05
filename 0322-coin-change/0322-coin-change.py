class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0 
        
        for coin in coins:
            for x in range(coin, amount +1):
                dp[x] = min(dp[x], dp[x-coin] +1 )
                
        return -1 if dp[-1] == float('inf') else dp[-1]
            
        