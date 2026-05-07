from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    result = 0
    d = deque([root])
    while d:
        result += 1
        for _ in range(len(d)):
            node = d.popleft()
            if node.left is None and node.right is None:
                return result
            if node.left is not None:
                d.append(node.left)
            if node.right is not None:
                d.append(node.right)


if __name__ == "__main__":
    res = minDepth(None)
    res