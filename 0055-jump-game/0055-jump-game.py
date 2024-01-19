class Solution(object):
    def canJump(self, nums):
        max_reach =0
        for i in range(len(nums)):
            max_reach = max(max_reach, nums[i] + i)
            if max_reach >= len(nums)-1:
                return True
            if max_reach == i:
                return False
        
        