class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        for idx, c in enumerate(s):
            for word in wordDict:
                n_w =len(word)
                if s[idx+1-n_w:idx+1] == word and dp[idx+1-n_w]:
                    dp[idx+1] = True
        
        return dp[-1]
        
        
        