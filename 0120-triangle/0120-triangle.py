class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for i in r] for r in triangle]
        dp[0][0] = triangle[0][0]
        
        for l in range(1, len(triangle)):
            row = triangle[l]
            for idx, num in enumerate(row):
                if idx == 0:
                    dp[l][idx] = dp[l-1][0] + num
                elif idx == len(row) -1:
                    dp[l][idx] = dp[l-1][-1] + num
                else:
                    dp[l][idx] = min(dp[l-1][idx], dp[l-1][idx-1]) + num
                    
        return min(dp[-1])