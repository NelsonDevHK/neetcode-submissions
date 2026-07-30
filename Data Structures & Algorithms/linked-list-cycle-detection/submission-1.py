# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastP = slowP = head 
        while fastP and fastP.next:
            fastP = fastP.next.next
            slowP = slowP.next
            
            if fastP == slowP:
                return True

        return False