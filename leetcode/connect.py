from typing import Optional, Deque


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f"{self.val}"

def connect(root: Optional[Node]) -> Optional[Node]:
    if root is None:
        return None
    q = Deque([root])
    while q:
        current = None
        for _ in range(len(q)):
            n = q.popleft()
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
            if current is not None:
                current.next = n
            current = n
    return root

if __name__ == "__main__":
    n9 = Node(val=9)
    n8 = Node(val=8, left=n9)
    n7 = Node(val=7)
    n6 = Node(val=6)
    n5 = Node(val=5)
    n4 = Node(val=4)
    n3 = Node(val=3, left=n6, right=n7)
    n2 = Node(val=2, left=n4, right=n5)
    n1 = Node(val=1, left=n2, right=n3)
    res = connect(n1)
    res