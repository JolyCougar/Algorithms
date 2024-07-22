# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.getHeight(root) >= 0

    def getHeight(self, tree):
        if tree is None:
            return 0
        left_height, right_height = self.getHeight(tree.left), self.getHeight(tree.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    result = Solution().isBalanced(root)
    print(result)

    root.left.left = TreeNode(2)
    result = Solution().isBalanced(root)
    print(result)
