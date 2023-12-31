# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        
        node = head
        while node:
            
            if visited.get(node, None):
                return True
            visited[node] = 1
            
            node = node.next
            
        return False
        