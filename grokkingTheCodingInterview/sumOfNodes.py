from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

def sum_of_nodes(root: TreeNode) -> int:
    if root is None:
        return 0
    _sum = 0
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        _sum += node.val
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)
    return _sum

def sum_of_nodes2(root: TreeNode) -> int:
    if root is None:
        return 0
    _sum = 0
    queue = [root]
    while queue:
        node = queue.pop(0)
        _sum += node.val
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return _sum


if __name__ == "__main__":
    node5 = TreeNode(6)
    node4 = TreeNode(2)
    node3 = TreeNode(7)
    node2 = TreeNode(9, node4, node5)
    node1 = TreeNode(4, node2, node3)
    res = sum_of_nodes(node1)
    res