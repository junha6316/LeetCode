class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        max_l = 0
        
        r, c = len(matrix), len(matrix[0])
        
    
            
        
        dp = [[0 for i in range(c)] for i in range(r)]
        
        for i in range(r):
            dp[i][0] = int(matrix[i][0])
            if matrix[i][0] == "1":
                max_l = 1
            
        for j in range(c):
            dp[0][j] = int(matrix[0][j])
            if matrix[0][j] == "1":
                max_l = 1
            
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    if dp[i][j] > max_l:
                        max_l = dp[i][j]
       
        
        answer = max_l * max_l     
        return answer
        