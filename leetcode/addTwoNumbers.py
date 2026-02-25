from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1, num2 = 0, 0
    pwr1, pwr2 = 0, 0
    n1, n2 = l1, l2
    while n1 is not None or n2 is not None:
        if n1 is not None:
            num1 += n1.val * 10 ** pwr1
            pwr1 += 1
            n1 = n1.next
        if n2 is not None:
            num2 += n2.val * 10 ** pwr2
            pwr2 += 1
            n2 = n2.next
    _sum = num1 + num2
    if _sum == 0:
        return ListNode(0)
    first = last = None
    while _sum > 0:
        val = _sum % 10
        node = ListNode(val)
        if first is None:
            first = last = node
        else:
            last.next = node
            last = node
        _sum //= 10
    return first

if __name__ == "__main__":
    n2 = ListNode(2)
    n1 = ListNode(1, n2)
    n4 = ListNode(4)
    n3 = ListNode(3, n4)
    res = addTwoNumbers(n1, n3)
    res