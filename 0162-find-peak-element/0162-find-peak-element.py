class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       
        if len(nums) == 1:
            return 0
        
        
    
        l, r  =0, len(nums)-1
        
        while l < r:
            pv = (l+r) // 2
            pv_elem = nums[pv]
            if pv > 0 and nums[pv] < nums[pv - 1]:
                r = pv - 1
            elif pv < len(nums) - 1 and nums[pv] < nums[pv + 1]:
                l = pv + 1
            else:
                return pv
            
        return l 
                
        