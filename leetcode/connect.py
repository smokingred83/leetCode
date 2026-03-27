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
    if root.left is not Node:
        connect_recur(root.left, root.right)
    return root

def connect_recur(left: Optional[Node], right: Optional[Node]):
    if left is None:
        return
    connect_recur(left.left, left.right)
    connect_recur(left.right, right.left)
    connect_recur(right.left, right.right)
    left.next = right


def connect1(root: Optional[Node]) -> Optional[Node]:
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
    n15 = Node(val=15)
    n14 = Node(val=14)
    n13 = Node(val=13)
    n12 = Node(val=12)
    n11 = Node(val=11)
    n10 = Node(val=10)
    n9 = Node(val=9)
    n8 = Node(val=8)
    n7 = Node(val=7, left=n14, right=n15)
    n6 = Node(val=6, left=n12, right=n13)
    n5 = Node(val=5, left=n10, right=n11)
    n4 = Node(val=4, left=n8, right=n9)
    n3 = Node(val=3, left=n6, right=n7)
    n2 = Node(val=2, left=n4, right=n5)
    n1 = Node(val=1, left=n2, right=n3)
    res = connect(n1)
    res