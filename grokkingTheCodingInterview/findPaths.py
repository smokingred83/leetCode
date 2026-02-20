from typing import Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

def add_paths(root: TreeNode, s: int, current: [int], all_paths: [int]):
    if root is None:
        return
    if root.val == s and root.left is None and root.right is None:
        all_paths.append(current + [root.val])
        return
    current.append(root.val)
    add_paths(root.left, s - root.val, current, all_paths)
    add_paths(root.right, s - root.val, current, all_paths)
    current.remove(root.val)

def find_paths(root: TreeNode, s: int) -> [int]:
    all_paths = []
    add_paths(root, s, [], all_paths)
    return all_paths


if __name__ == "__main__":
    node8 = TreeNode(2)
    node6 = TreeNode(10, None, None)
    node7 = TreeNode(5)
    node5 = TreeNode(6)
    node4 = TreeNode(4)
    node3 = TreeNode(1, node6, node7)
    node2 = TreeNode(7, node4, None)
    node1 = TreeNode(12, node2, node3)
    res = find_paths(node1, 18)
    res