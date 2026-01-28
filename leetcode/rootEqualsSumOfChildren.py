# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root: Optional[TreeNode]) -> bool:
    return root.val == root.left.val + root.right.val

if __name__ == '__main__':
    res = checkTree(TreeNode(10, left=TreeNode(4), right=TreeNode(6)))
    res