class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 회전된 수를 찾고, 회전된 수  r % n + 1
        n = len(nums)
        
        left, right = 0, len(nums)-1
        
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
                
        
        peak_idx = left
        
        
        return nums[peak_idx]
        