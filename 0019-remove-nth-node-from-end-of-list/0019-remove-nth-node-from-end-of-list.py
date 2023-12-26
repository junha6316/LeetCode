# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        
        n = length - n
        idx = 1
        node = head
        prev = None
        
        while node:
            if n == idx:
                if prev is None: 
                    return head.next
                elif node.next is None: # 맨처음 인덱스 제거시
                    prev.next = None
                    return head
                elif prev.next and node.next:
                    prev.next = node.next
                    return head
            
            idx += 1
            prev = node
            node = node.next
            
        
    def getLength(self, head):
        length = 1
        node =head
        while node:
            length += 1
            node = node.next
        return length
        
    
  