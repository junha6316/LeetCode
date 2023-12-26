class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        answer = 0
        
        for num in num_set:
            
            if num -1 not in num_set:
                cur_num = num
                local_streak = 1
                while cur_num + 1 in num_set:
                    local_streak += 1
                    cur_num += 1
                    
                answer = max(answer, local_streak)
        return answer
                
            
        
        

        
        