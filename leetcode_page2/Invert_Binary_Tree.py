# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# -------------------------------------------
# stack = [root]
# while stack:
#     node = stack.pop(-1)
#     if node:
#         node.left, node.right = node.right, node.left
#         stack.append(node.left)
#         stack.append(node.right)
# return root
