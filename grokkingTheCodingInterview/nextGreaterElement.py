def next_greater_element(nums1: [int], nums2: [int]) -> [int]:
    res = [0] * len(nums1)
    stack = []
    idx1 = len(nums1) - 1
    for i in range(len(nums2) - 1, -1, -1):
        while stack and stack[-1] <= nums1[idx1]:
            stack.pop()
        if stack:
            res[idx1] = stack[-1]
            idx1 -= 1
        stack.append(nums2[i])
    return res

if __name__ == "__main__":
    res = next_greater_element([4,2,6], [6,2,4,5,3,7])
    res