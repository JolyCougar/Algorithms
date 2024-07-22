# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        else:
            if targetSum == root.val and root.left is None and root.right is None:
                return True
            else:
                return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right,
                                                                                           targetSum - root.val)
    # ---------------------------------
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     # dfs
    #     if root is None:
    #         return False
    #
    #     def search(node, runSum):
    #         # print(f'on node {node.val}, runSum is: {runSum}')
    #         if node.left is None and node.right is None:  # and node.val + runSum == targetSum:
    #             # print(f'on left {node.val}, condition {node.val + runSum} == {targetSum}')
    #             if node.val + runSum == targetSum:
    #                 # print('return True')
    #                 return True
    #
    #         if node.left:
    #             if search(node.left, runSum + node.val):
    #                 return True
    #         if node.right:
    #             if search(node.right, runSum + node.val):
    #                 return True
    #
    #     res = search(root, 0)
    #     return res == True
