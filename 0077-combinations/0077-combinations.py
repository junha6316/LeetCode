class Solution(object):
     def combine(self, n, k):
        answer = []
        def btrk(cur):
            if len(cur) == k:
                answer.append(cur[:])
                return
            
            last = cur[-1] 
            need = k - len(cur)
            remain = n - (last+1) + 1
            available = remain - need
            
            for i in range(last+1, last+1 + available +1):
                cur.append(i)
                btrk(cur)
                cur.pop()
                
        for i in range(1, n+1):
            btrk([i])
        return answer
            
        
        
        