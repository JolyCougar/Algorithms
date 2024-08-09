# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        result = str()
        while dummy.next:
            result += str(dummy.next.val)
            dummy = dummy.next
        return result == result[::-1]

# ------------------------------------------------------------------
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         rev = None
#         slow = fast = head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow_next = slow.next
#             slow.next = rev
#             rev = slow
#             slow = slow_next
#         if fast:
#             slow = slow.next
#         while rev:
#             if rev.val != slow.val:
#                 return False
#             slow = slow.next
#             rev = rev.next
#         return True
