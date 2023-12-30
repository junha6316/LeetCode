"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None:
            return None
        
        dummy = Node('test')
        prev = dummy
        q = [(0,  root,)]
        cur_d =0
        
        while q:
            # print([(d, node.val) for d, node in q])
            d,  node = q.pop(0)
            
            if d != cur_d:
                cur_d = d
                l_node= Node("#")
                prev.next = None
                
            else:
                prev.next = node
                
            prev = node
            
            if node.left:
                q.append([d+1, node.left])
            if node.right:
                q.append([d+1, node.right])
                
       
        return dummy.next
            
                
                
                
            
            
            
        