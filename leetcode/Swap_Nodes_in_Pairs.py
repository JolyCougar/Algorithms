# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one
        return dummy.next


# -------------------------------------------------------------------------------------------------------
# if not head or not head.next:
#     return head
# newHead = ListNode()
# prev = newHead
# node = head
# prev.next = node
# while node and node.next:
#     prev.next = node.next
#     node.next = node.next.next
#     prev = prev.next
#     prev.next = node
#     prev = node
#     node = node.next
# return newHead.next
