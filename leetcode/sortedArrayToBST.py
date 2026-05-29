from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

def to_bst(nums: List[int], s: int, e: int) -> Optional[TreeNode]:
    if e - s < 0:
        return None
    m = (s + e) // 2
    return TreeNode(
        nums[m], to_bst(nums, s, m - 1), to_bst(nums, m + 1, e))


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    return to_bst(nums, 0, len(nums) - 1)

if __name__ == "__main__":
    res = sortedArrayToBST([-10,-3,0,5,9])
    res