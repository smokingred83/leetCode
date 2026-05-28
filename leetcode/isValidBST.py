from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

def check_min_max(root: Optional[TreeNode], _min: float | int, _max: float | int) -> bool:
    if root is None:
        return True
    left = check_min_max(root.left, _min, root.val)
    right = check_min_max(root.right, root.val, _max)
    return left and right and _min < root.val < _max

def isValidBST(root: Optional[TreeNode]) -> bool:
    return check_min_max(root, -inf, inf)

def isValidBST_stack(root: Optional[TreeNode]) -> bool:
    stack = []
    collect(root, stack)
    for _ in range(len(stack) - 1):
        node = stack.pop()
        if node <= stack[-1]:
            return False
    return True

def collect(node: Optional[TreeNode], stack: [int]):
    if node is None:
        return
    collect(node.left, stack)
    stack.append(node.val)
    collect(node.right, stack)

if __name__ == "__main__":
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node6 = TreeNode(6, node4, node7)
    node5 = TreeNode(5, node1, node6)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    res = isValidBST(node5)
    res
