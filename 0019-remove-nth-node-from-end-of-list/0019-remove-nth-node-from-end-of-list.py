# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head=self.reversell(head)
        idx = 1
        node = head
        prev = None
        
        while node:
            if idx == n:
                if prev is None: 
                    return self.reversell(head.next)
                elif node.next is None: # 맨처음 인덱스 제거시
                    prev.next = None
                    return self.reversell(head) # 
                elif prev.next and node.next:
                    prev.next = node.next
                break
                    
            idx += 1
            prev = node
            node = node.next
        
        if prev is None:    
            return None
        return self.reversell(head)
    
    def reversell(self, node):
        cur = node
        prev = None
        
        while cur:
            next_node = cur.next
            
            cur.next = prev
            prev = cur
            cur = next_node
        
        return prev