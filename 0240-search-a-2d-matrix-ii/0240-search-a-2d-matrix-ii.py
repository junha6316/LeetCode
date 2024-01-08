class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tmp = []
        for r in matrix:
            tmp.extend(r)
            
        return target in tmp
        