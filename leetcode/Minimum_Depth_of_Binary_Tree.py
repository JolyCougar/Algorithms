# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        depth = 1
        return self.getMinDepth(root, depth)

    def getMinDepth(self, root, depth):
        if root is None:
            return depth - 1

        left_Depth = self.getMinDepth(root.left, depth + 1)
        right_Depth = self.getMinDepth(root.right, depth + 1)
        if left_Depth == depth:
            return right_Depth
        if right_Depth == depth:
            return left_Depth
        return min(left_Depth, right_Depth)


# ---------------------------------------------------------------
# if not root:
#     return 0
#
# q = deque()
# q.append(root)
#
# floor = 0
# while q:
#     q_size = len(q)
#     floor += 1
#
#     for _ in range(q_size):
#         node = q.popleft()
#
#         if not node.left and not node.right:
#             return floor
#
#         if node.left: q.append(node.left)
#         if node.right: q.append(node.right)
#
# return floor
