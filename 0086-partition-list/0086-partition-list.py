# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        tmp =[]
        
        prehead = ListNode(0)
        prev = prehead
        prev.next = head
        node = head
            
        while node:
            if node.val < x:
                tmp.append(node)
                prev.next = node.next
                node = node.next
                
            else:
                prev = node        
                node = node.next
                
        for i in range(len(tmp)-1):
            tmp[i].next = tmp[i+1]
        
        if len(tmp) > 0:
            t = prehead.next
            prehead.next = tmp[0]
            tmp[-1].next = t

            
            
            
        
                
        return prehead.next
            
            
        
        
        
        
        
        