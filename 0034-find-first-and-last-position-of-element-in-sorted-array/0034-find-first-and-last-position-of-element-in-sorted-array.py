class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        이분 탐색 2번 하면 될거 같음
        1. 왼쪽 우선
        2. 오른쪽 우선
        """
        
        n = len(nums)
        L_end, r_end = -1, -1
        def searchLow(nums, target):
            l, r = 0, n-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] >= target:
                    # 같을 때도 오른쪽 범위를 버려서 왼쪽 끝을 찾음
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        def searchHigh(nums, target):
            l, r = 0, n-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    # 같을 때는 왼쪽 범위를 버려서 오른쪽 끝을 찾음
                    l = mid + 1
            return r
                
        l_end = searchLow(nums, target)
        r_end = searchHigh(nums, target)
        
        if 0 <= l_end <= n and l_end<= r_end and nums[l_end] == target:
            return [l_end, r_end]
        return [-1,-1]
        