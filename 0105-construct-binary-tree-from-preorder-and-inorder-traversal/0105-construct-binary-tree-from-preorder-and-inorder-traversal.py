# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self._buildTree(preorder, inorder)
        
        
    def _buildTree(self, preorder, inorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        root_idx = inorder.index(root.val)
        
        l_tree = inorder[:root_idx]
        r_tree = inorder[root_idx+1:]
        
        root.left = self._buildTree(preorder, l_tree) if l_tree else None
        
        root.right = self._buildTree(preorder, r_tree) if r_tree else None
        
        return root
        
        
        
        
        