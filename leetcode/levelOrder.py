from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    if root is None:
        return result

    q = deque([root])
    while q:
        tmp = []
        for _ in  range(len(q)):
            n = q.popleft()
            tmp.append(n.val)
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
        result.append(tmp)

    return result


if __name__ == "__main__":
    n7 = TreeNode(val=7)
    n6 = TreeNode(val=6)
    n5 = TreeNode(val=5)
    n4 = TreeNode(val=4)
    n3 = TreeNode(val=3, left=n6, right=n7)
    n2 = TreeNode(val=2, left=n4, right=n5)
    n1 = TreeNode(val=1, left=n2, right=n3)
    res = levelOrder(n1)
    res