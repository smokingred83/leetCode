from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    current, prev = head, None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

if __name__ == "__main__":
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    res = reverseList(n1)
    res