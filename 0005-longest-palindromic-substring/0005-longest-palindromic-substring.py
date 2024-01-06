class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        answer = [0,0]
        
        dp = [[False for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            dp[i][i] = True
            
        for i in range(N-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                answer = [i, i+1]
                
        for diff in range(2, N):
        
            for i in range(N-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] =True
                    answer = [i, j]
        i, j = answer
                    
        return s[i: j+1]
                
        