# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = [(0,root)]
        answer ={}
        
        while q:
            d, node = q.pop(0)
            
            if answer.get(d, None) is None:
                answer[d] = [node.val]
            else:
                answer[d].append(node.val)
                
            
            if node.left:
                q.append((d+1, node.left))
            
            if node.right:
                q.append((d+1, node.right))
                
        
        return answer.values()
                
                
            
       
        
        
        
        
        