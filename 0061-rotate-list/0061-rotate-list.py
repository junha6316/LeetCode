# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        node = head
        length = 0
        while node:
            length +=1
          
            if node.next:
                node = node.next
            else:
                node.next = head
                break
            
                
                
        
        k = k % length
        k = length - k
        
        
        while k > 1:
            head = head.next
            k -=1
        
        answer = head.next
        head.next = None
        
        
        return answer
            
                
                
        
            
        
        
        
        