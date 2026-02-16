from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


def zig_zag_traverse(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    reverse = False
    while queue:
        lvl_size = len(queue)
        tmp = deque()
        for _ in range(lvl_size):
            n = queue.popleft()
            tmp.appendleft(n.val) if reverse else tmp.append(n.val)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        result.append(list(tmp))
        reverse = not reverse
    return result

def zig_zag_traverse2(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    reverse = False
    while queue:
        lvl_size = len(queue)
        tmp = []
        for _ in range(lvl_size):
            n = queue.popleft()
            tmp.append(n.val)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        result.append([tmp.pop() for _ in range(len(tmp))]) if reverse\
            else result.append(tmp)
        reverse = not reverse
    return result


if __name__ == "__main__":
    node6 = TreeNode(5)
    node7 = TreeNode(8)
    node5 = TreeNode(6)
    node4 = TreeNode(2)
    node3 = TreeNode(7, node6, node7)
    node2 = TreeNode(9, node4, node5)
    node1 = TreeNode(4, node2, node3)
    res = zig_zag_traverse(node1)
    res