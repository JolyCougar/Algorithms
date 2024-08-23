# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = head = ListNode()
        carry = 0
        while l1 and l2:
            carry, cur = divmod(l1.val + l2.val + carry, 10)
            node = ListNode(cur)
            head.next = node
            head, l1, l2 = head.next, l1.next, l2.next
        head.next = l1 if l1 else l2
        while carry and head.next:
            carry, cur = divmod(head.next.val + carry, 10)
            head.next.val = cur
            head = head.next
        if carry:
            head.next = ListNode(carry)
        return result.next


# -------------------------------------------------------------------------------------------------
# carry = 0
# newList = ListNode(None)
#
# hd = newList
#
# while l1 or l2:
#
#     if l1 and l2:
#         val = ((l1.val + l2.val) + carry) % 10
#
#         carry = ((l1.val + l2.val) + carry) // 10
#
#         newList.next = ListNode(val)
#
#         newList = newList.next
#
#     elif l1:
#
#         val = (l1.val + carry) % 10
#
#         carry = (l1.val + carry) // 10
#
#         newList.next = ListNode(val)
#
#         newList = newList.next
#
#     elif l2:
#
#         val = (l2.val + carry) % 10
#
#         carry = (l2.val + carry) // 10
#
#         newList.next = ListNode(val)
#
#         newList = newList.next
#
#     if l1:
#         l1 = l1.next
#
#     if l2:
#         l2 = l2.next
#
# if carry:
#     newList.next = ListNode(carry)
#
# return hd.next
