# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        q = [root]
        
        answer = 0
        while q:
            node = q.pop(0)

            answer += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return answer
        