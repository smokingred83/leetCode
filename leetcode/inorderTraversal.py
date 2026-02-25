from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

def inorderTraversal(root: Optional[TreeNode]) -> [int]:
    if root is None:
        return []
    go_left = True
    res, stack = [], [root]
    while stack:
        node = stack[-1]
        if go_left:
            if node.left:
                stack.append(node.left)
            else:
                go_left = False
        else:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
                go_left = True
    return res

if __name__ == "__main__":
    n9 = TreeNode(val=9)
    n8 = TreeNode(val=8, left=n9)
    n7 = TreeNode(val=7)
    n6 = TreeNode(val=6)
    n5 = TreeNode(val=5, left=n6, right=n7)
    n4 = TreeNode(val=4)
    n3 = TreeNode(val=3, right=n8)
    n2 = TreeNode(val=2, left=n4, right=n5)
    n1 = TreeNode(val=1, left=n2, right=n3)
    res = inorderTraversal(n1)
    res