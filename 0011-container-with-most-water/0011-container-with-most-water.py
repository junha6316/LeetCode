class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        N = len(height)
        l =0
        r = N -1
        
        answer =0
        while l < r:
            
            a = min(height[l], height[r]) * (r-l)
            
            if a > answer:
                answer = a
            
            if height[l] > height[r]:
                r -= 1
            else:
                l+= 1
                
        return answer
        