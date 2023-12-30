# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._inorderd = []
        self._inorder(root)
        
        

    def next(self) -> int:
        return self._inorderd.pop(0)
        

    def hasNext(self) -> bool:
        return len(self._inorderd) > 0
        
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            self._inorderd.append(node.val)
            self._inorder(node.right)
        
            
            
            
            

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()