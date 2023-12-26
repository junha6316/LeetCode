class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        # 배열의 각 요소에 대해 확인합니다.
        for num in num_set:
            # 현재 숫자가 연속 수열의 시작점인지 확인합니다.
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 다음 연속 숫자가 존재하는지 확인하면서 길이를 증가시킵니다.
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # 최대 길이를 업데이트합니다.
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
                
                
            
        
        

        
        