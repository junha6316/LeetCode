# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self._buildTree(inorder, postorder)
        
        
        
    def _buildTree(self, inorder, postorder):
        if not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        root_idx = inorder.index(root.val)
        
        l_t = inorder[:root_idx]
        r_t = inorder[root_idx+1:]
        
        root.right = self._buildTree(r_t, postorder) if r_t else None
        root.left = self._buildTree(l_t, postorder) if l_t else None
        
        
        
        return root
        
            
        