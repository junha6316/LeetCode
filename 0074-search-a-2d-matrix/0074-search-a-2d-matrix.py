class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tmp = []
        
        for i in matrix:
            tmp.extend(i)
            
        return target in tmp