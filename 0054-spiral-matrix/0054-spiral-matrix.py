class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.answer =[]
        mode = 1
        while matrix:
            if mode == 1:
                self.mode1(matrix)
                mode += 1
            elif mode == 2:
                self.mode2(matrix)
                mode += 1
            elif mode == 3:
                self.mode3(matrix)
                mode += 1
            elif mode ==4:
                self.mode4(matrix)
                mode = 1
                
        return self.answer
    
    def mode1(self, matrix):
        self.answer.extend(matrix.pop(0))
        
    def mode2(self, matrix):
        tmp = []
        
        for row in matrix:
            if  len(row) >0:
                tmp.append(row.pop())
        
        self.answer.extend(tmp)
    def mode3(self, matrix):
        last_row = matrix.pop()
        self.answer.extend(last_row[::-1])
        
    def mode4(self, matrix):
        tmp = []
        for idx in range(len(matrix)-1, -1, -1):
            row = matrix[idx]
            if len(row) > 0:
                tmp.append(row.pop(0))
        self.answer.extend(tmp)
        
    
        
            
        