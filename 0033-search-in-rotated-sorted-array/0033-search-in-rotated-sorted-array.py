class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        
        rotate_num = left
        
        tmp = nums[left:] + nums[:left]
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if tmp[mid] == target:
                return (mid + rotate_num) % n
            
            elif tmp[mid] > target:
                right = mid - 1
                
            elif tmp[mid] < target:
                left = mid + 1
        return -1
        
        
        
                
                
                