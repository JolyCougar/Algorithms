# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy

        for i in range(n):
            first = first.next

        while first.next is not None:
            first = first.next
            second = second.next
        else:
            second.next = second.next.next

        return dummy.next


# -------------------------------------------------------------------
# slow, fast = head, head
#
# for i in range(n):
#     fast = fast.next
#
# if not fast:
#     return head.next
#
# while fast.next:
#     slow = slow.next
#     fast = fast.next
#
# slow.next = slow.next.next
#
# return head
