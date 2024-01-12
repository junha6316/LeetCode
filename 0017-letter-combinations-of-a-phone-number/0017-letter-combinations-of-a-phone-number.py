class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.mapping = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            '5': 'jkl',
            "6":'mno',
            "7":'pqrs',
            "8":'tuv',
            "9":'wxyz'
        }
        if digits:
            return self._r(digits, "")
        
        return []
      
    def _r(self, digits, cur):
        if len(digits) == 0:
            return [cur]
        
        result =[]
        d = digits[0]
        nums = self.mapping[d]
        for num in nums:
            r = self._r(digits[1:], cur+num)
            result.extend(r)
        return result
        
        
            
            
            
        