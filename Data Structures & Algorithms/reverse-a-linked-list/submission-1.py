# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we can solve this question with two pointer
        # prev and cur if cur next is None
        cur ,prev = head, None
        while cur:
            nxt = cur.next # aka head.next in first layer
            cur.next = prev
            prev = cur
            cur = nxt
        return prev