# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None
        current = head

        while current:
            next_node = current.next  # 다음 노드를 임시로 저장
            current.next = previous  # 현재 노드의 다음을 이전 노드로 변경
            previous = current  # 이전 노드를 현재 노드로 업데이트
            current = next_node  # 현재 노드를 다음 노드로 이동
            
        return previous
