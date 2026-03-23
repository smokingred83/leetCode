from typing import Optional


class ListNode:
    def __init__(self, x, n = None):
        self.val = x
        self.next = n

    def __repr__(self):
        return f'{self.val}'

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if headA is None or headB is None:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a is not None else headB
        b = b.next if b is not None else headA
    return a


def getIntersectionNode1(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if headA is None or headB is None:
        return None
    a, b, length_a, length_b = headA, headB, 1, 1
    while a.next is not None:
        length_a += 1
        a = a.next
    while b.next is not None:
        length_b += 1
        b = b.next
    if a != b:
        return None
    diff = abs(length_a - length_b)
    a, b = headA, headB
    if length_a > length_b:
        for _ in range(diff):
            a = a.next
    elif length_b > length_a:
        for _ in range(diff):
            b = b.next
    while a != b:
        a = a.next
        b = b.next
    return a

def getIntersectionNode2(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    a, b = headA, headB
    seen = set()
    while a is not None:
        seen.add(a)
        a = a.next
    while b is not None:
        if b in seen:
            return b
        b = b.next
    return None

if __name__ == "__main__":
    n5b = ListNode(5)
    n4a = ListNode(4, n5b)
    n8 = ListNode(8, n4a)
    n1a = ListNode(1, n8)
    n6 = ListNode(6, n1a)
    n5a = ListNode(5, n6)
    n1b = ListNode(1, n8)
    n4b = ListNode(4, n1b)
    res = getIntersectionNode(n4b, n5a)
    res