class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1 for _ in range(N)]
        answer = 0
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] =max(dp[i], dp[j]+1)
            answer = max(answer, dp[i])
        
        return answer

        
        