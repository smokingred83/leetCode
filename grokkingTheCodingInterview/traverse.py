from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

def traverse(root: TreeNode) -> [TreeNode]:
    if root is None:
        return []
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        tmp = []
        for _ in range(level_size):
            node = queue.popleft()
            tmp.append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(tmp)
    return result

def traverse2(root: TreeNode) -> [TreeNode]:
    if root is None:
        return []
    result = [[]]
    block = TreeNode()
    queue = deque([root, block])

    while len(queue) > 1:
        node = queue.popleft()
        if node == block:
            result.append([])
            queue.append(block)
        else:
            result[-1].append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return result

if __name__ == "__main__":
    node6 = TreeNode(5)
    node7 = TreeNode(8)
    node5 = TreeNode(6)
    node4 = TreeNode(2)
    node3 = TreeNode(7, node6, node7)
    node2 = TreeNode(9, node4, node5)
    node1 = TreeNode(4, node2, node3)
    res = traverse(node1)
    res