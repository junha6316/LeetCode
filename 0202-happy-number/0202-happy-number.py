class Solution:
    def isHappy(self, n: int) -> bool:
        self.memo = {}
        return self._cal(n)
        
        
        
    
    def _cal(self, n):
        cnt = self.memo.get(n, None)
        
        if cnt:
            return False
        tmp = 0
        for i in str(n):
            tmp += int(i) * int(i)
            
        self.memo[n] = tmp
        if tmp == 1:
            return True
            
        return self._cal(tmp)
            
        
            
        
            
        
    