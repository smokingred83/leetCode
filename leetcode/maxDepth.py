from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

if __name__ == "__main__":
    node2 = TreeNode(2)
    node1 = TreeNode(1, left=node2)
    res = maxDepth(node1)
    res