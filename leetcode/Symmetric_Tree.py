# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = list()
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            left, right = stack.pop(), stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)

            stack.append(left.right)
            stack.append(right.left)

        return True
