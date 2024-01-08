class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        
        if m == 0:
            return False
        
        n = len(matrix[0])
        
        l, r = 0, m*n-1
        while l <= r:
            pv = (l+r) // 2
            pv_elem = matrix[pv //n][pv %n]
            if target == pv_elem:
                return True
            else:
                if target < pv_elem:
                    r = pv -1
                else:
                    l = pv + 1
                    
        return False
            