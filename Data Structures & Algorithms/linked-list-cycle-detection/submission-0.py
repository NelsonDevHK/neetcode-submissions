# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastP ,slowP = head,head 
        while fastP is not None and fastP.next is not None:
            fastP = fastP.next.next
            slowP = slowP.next
            if fastP and fastP.val == slowP.val:
                return True
        return False