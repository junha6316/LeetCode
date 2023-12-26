# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        
            
        
        return self.reverseLinkedList(head, left, right)

    def reverseLinkedList(self, head,m,n):
        if not head or m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # m번째 노드까지 이동
        for _ in range(m - 1):
            prev = prev.next
        start = prev.next
        then = start.next

        # 노드 뒤집기
        for _ in range(n - m):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next
        
            
            
            
        

     
            
            
            

        
"""

1 2 3 4 5 

4, 5
3, 4

tmp 5

3, 5
4, 3

tmp = 5
4, 4
3, 5

"""