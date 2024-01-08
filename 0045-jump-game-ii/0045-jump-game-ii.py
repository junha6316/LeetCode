class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_st, cur_fa = 0,0
        answer = 0
        
        for i in range(len(nums)-1):
            jump = nums[i]
        
            cur_fa = max(cur_fa, jump+i)
            
            if i == cur_st:
                answer +=1
                cur_st = cur_fa
                
        
        return answer
        
        