from typing import List


def removeDuplicates(nums: List[int]) -> int:
    l = len(nums)
    if l < 2:
        return l
    p1, p2 = 0, 1
    while p2 < l:
        if nums[p1] != nums[p2]:
            nums[p1 + 1] = nums[p2]
            p1 += 1
        p2 += 1
    return p1 + 1

if __name__ == "__main__":
    res = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    res