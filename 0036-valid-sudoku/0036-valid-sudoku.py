class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        
        for x in range(9):
            for y in range(9):
                if not self._is_valid_in_row(x,y):
                    return False
                
        for x in [0, 3, 6]:
            for y in [0,3,6]:
                tmp = []
                for row in self.board[y:y+3]:
                    tmp.extend([c for c in row[x: x+3] if c != "."])
                
                if len(set(tmp)) != len(tmp):
                    return False
                
                
                
                
                
                
               
        
                
        return True
                    
    
    
    def _is_valid_in_row(self, x, y):
        row = [c for c in self.board[y] if c != "."]
        col = [row[x] for row in self.board if row[x] != "."]
        
        
        # square inculded x,,y
        
        return len(row) == len(set(row)) and len(col) == len(set(col))
        
        
        