# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
            elif p or q:
                return False
        return True

        # if p is None and q is None:
        #     return True
        # if p is not None and q is not None:
        #     return p.val == q.val and (self.isSameTree(p.left,q.left)) and self.isSameTree(p.right, q.right)
        # return False
