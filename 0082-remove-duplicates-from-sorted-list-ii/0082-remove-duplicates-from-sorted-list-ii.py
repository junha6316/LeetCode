# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        
        
        prehead = ListNode(-1)
        prehead.next = head
        prev = head
        node= prehead
        
        while node:
            next_node = node.next
            
            if next_node and next_node.val == node.val:
                while next_node and next_node.val == node.val:
                    prev.next = next_node.next
                    next_node = next_node.next
                node = next_node
                    
            else:
                

                
            
                prev = node
                node = node.next

        
        return prehead.next
            
        