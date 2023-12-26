class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        answer = 0
        
        for num in num_set:
            if num -1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:    
                    current_num += 1
                    current_streak += 1
                
                answer = max(answer, current_streak)
        
        return answer
                
                
            
        
        

        
        