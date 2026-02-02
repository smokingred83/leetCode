from utils.my_tree_node import MyTreeNode


def create_minimal_bst(arr: [int]) -> MyTreeNode:
    return create_minimal_bst_recursive(arr, 0, len(arr) - 1)

def create_minimal_bst_recursive(arr: [int], start: int, end: int) -> MyTreeNode:
    if start > end:
        return None
    middle = (start + end) // 2
    parent = MyTreeNode(arr[middle])
    parent.left = create_minimal_bst_recursive(arr, start, middle - 1)
    parent.right = create_minimal_bst_recursive(arr, middle + 1, end)
    return parent


def create_minimal_bst_no_recursive(arr: [int]):
    middle = len(arr) // 2
    parent = root = MyTreeNode(arr[middle])
    for i in range(middle - 2, -1, -2):
        left = MyTreeNode(arr[i])
        parent.left = left
        right = MyTreeNode(arr[i + 1])
        left.right = right
        parent = left
    if parent.data is not arr[0]:
        parent.left = MyTreeNode(arr[0])
    parent = root
    for i in range(middle + 2, len(arr), 2):
        right = MyTreeNode(arr[i])
        parent.right = right
        left = MyTreeNode(arr[i - 1])
        right.left = left
        parent = right
    if parent.data is not arr[-1]:
        parent.right = MyTreeNode(arr[-1])
    return root

if __name__ == "__main__":
    res = create_minimal_bst([2, 4, 6, 8, 10, 12, 14, 16, 18])
    res