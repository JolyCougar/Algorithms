# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# -------------------------------------------------
# if root is None:
#     return 0
#
# node, level = root, 0
# while node.left is not None:
#     node = node.left
#     level += 1
#
# # Binary search.
# left, right = 2 ** level, 2 ** (level + 1)
# while left < right:
#     mid = left + (right - left) / 2
#     if not self.exist(root, mid):
#         right = mid
#     else:
#         left = mid + 1
#
# return left - 1
#
#
# # Check if the nth node exist.
# def exist(self, root, n):
#     k = 1
#     while k <= n:
#         k <<= 1
#     k >>= 2
#
#     node = root
#     while k > 0:
#         if (n & k) == 0:
#             node = node.left
#         else:
#             node = node.right
#         k >>= 1
#     return node is not None
