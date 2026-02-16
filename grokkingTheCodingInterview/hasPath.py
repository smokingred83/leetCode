class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

def has_path(root, s) -> bool:
    if root is None:
        return False
    current = s - root.val
    if root.left is None and root.right is None:
        return current == 0
    return has_path(root.left, current) or has_path(root.right, current)


if __name__ == "__main__":
    node8 = TreeNode(2)
    node6 = TreeNode(10, node8, None)
    node7 = TreeNode(18)
    node5 = TreeNode(6)
    node4 = TreeNode(2)
    node3 = TreeNode(12, node6, node7)
    node2 = TreeNode(40, None, None)
    node1 = TreeNode(8, node2, node3)
    res = has_path(node1, 32)
    res