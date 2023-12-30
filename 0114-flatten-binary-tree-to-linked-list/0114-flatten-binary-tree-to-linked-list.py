# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preorder(root)
        
    def preorder(self, node):
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            
            tmp = node.right
            node.right = node.left
            node.left = None
            if node.right:
                tmp_node = node.right
                while tmp_node:
                    if tmp_node.right is None:
                        tmp_node.right = tmp
                        break
                        
                    tmp_node = tmp_node.right

                
            else:
                node.right = tmp
            


            
                
        