from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

def print_level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        level_size = len(queue)
        tmp = ""
        for _ in range(level_size):
            n = queue.popleft()
            tmp += f"{n.val} "
            if n.left is not None:
                queue.append(n.left)
            if n.right is not None:
                queue.append(n.right)
        print(f"{tmp}")

if __name__ == "__main__":
    node6 = TreeNode(5)
    node7 = TreeNode(8)
    node5 = TreeNode(6)
    node4 = TreeNode(2)
    node3 = TreeNode(7, node6, node7)
    node2 = TreeNode(9, node4, node5)
    node1 = TreeNode(4, node2, node3)
    res = print_level_order(node1)
    res