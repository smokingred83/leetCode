from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    left = nums1[0:m]
    right = nums2[0:n]
    c, l, r = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            nums1[c] = left[l]
            l += 1
        else:
            nums1[c] = right[r]
            r += 1
        c += 1
    while l < m:
        nums1[c] = left[l]
        l += 1
        c += 1
    while r < n:
        nums1[c] = right[r]
        r += 1
        c += 1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    res = merge(nums1, 3, [2,5,6], 3)
    res

