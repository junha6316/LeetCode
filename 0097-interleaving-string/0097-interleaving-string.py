class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 + n2 != len(s3):
            return False
        
        if n1 == 0 or n2 ==0:
            if n1 == 0:
                return s3== s2
            if n2 ==0:
                return s3 ==s1
        
        dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        dp[0][0] =True
        
        
        for i in range(n1+1):
            for j in range(n2+1):
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]: # s1, s3입장에서는 -1를 해줘야 맞는 인덱스가 들어감
                    dp[i][j] = True
                
                if dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
                    
        return dp[n1][n2]