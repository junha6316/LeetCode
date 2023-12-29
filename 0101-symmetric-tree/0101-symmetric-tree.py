# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print('')
        q_l = [root.left]
        q_r = [root.right]
        
        while q_l and q_r:
            l, r = q_l.pop(0), q_r.pop(0)
            if l is None and r is None:
                continue
                
            if l is None and r or r is None and l:
                return False
            
            if l.val != r.val:
                return False
            

            q_l.append(l.left)
            q_r.append(r.right)


            q_l.append(l.right)
            q_r.append(r.left)
            

        return True
            
            
            
            
            
            
            
            
            
            
            
            
        


    


    
    
        


    
    
        