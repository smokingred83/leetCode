class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

def removeNodes(head):
    stack = []
    while head is not None:
        while len(stack) > 0 and head.val > stack[-1].val:
            stack.pop()
        if len(stack) > 0:
            stack[-1].next = head
        stack.append(head)
        head = head.next
    return stack[0]

if __name__ == "__main__":
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(5, n4)
    n2 = ListNode(4, n3)
    n1 = ListNode(5, n2)
    res = removeNodes(n1)
    res