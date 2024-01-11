class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [1 for i in range(len(nums)+1)]
        dp[0] = 0
        
        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    dp[i+1] = max(dp[j+1]+1, dp[i+1])
        
                    
        return max(dp)

        
        