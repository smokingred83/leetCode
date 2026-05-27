from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

def mergeTwoLists_recur(current: Optional[ListNode], next: Optional[ListNode]):
    if not current:
        return
    if next and current.val <= next.val:
        tmp = current.next
        if not tmp or tmp.val > next.val:
            current.next = next
        mergeTwoLists_recur(tmp, next)
    else:
        mergeTwoLists_recur(next, current)

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    mergeTwoLists_recur(list1, list2)
    return list2 if list2 and list1.val > list2.val else list1

def mergeTwoLists_iter(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2

    current, next = list1, list2
    while current and next:
        if current.val <= next.val:
            tmp = current.next
            if not tmp or tmp.val > next.val:
                current.next = next
            current = tmp
        else:
            current, next = next, current

    return list2 if list2 and list1.val > list2.val else list1


if __name__ == '__main__':
    n4 = ListNode(4)
    n6 = ListNode(4)
    n3 = ListNode(3, n6)
    n5 = ListNode(1, n3)
    n2 = ListNode(2, n4)
    n1 = ListNode(1, n2)
    res = mergeTwoLists_iter(n1, n5)
    res