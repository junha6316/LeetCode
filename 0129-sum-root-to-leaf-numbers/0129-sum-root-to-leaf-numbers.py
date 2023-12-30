# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = []
        q = [('', root)]
        
        while q:
            prev, node = q.pop(0)
            
            cur= prev+ str(node.val)
            
            if node.left:
                q.append([cur, node.left])
            if node.right:
                q.append([cur, node.right])
                
            if not node.left and not node.right:
                answer.append(int(cur))
                
        return sum(answer)
                