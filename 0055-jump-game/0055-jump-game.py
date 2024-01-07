class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i in range(len(nums)):
            if max_reach < i:
                return False  # Return false if you're stuck before reaching the end
            
            max_reach = max(max_reach, i + nums[i])  # Update the maximum reach
        
        # Check if you've reached or exceeded the last index
        return max_reach >= len(nums) - 1
            
            
            
        