def next_greater_element(nums1: [int], nums2: [int]) -> [int]:
    res = [-1] * len(nums1)
    num2idx = {n: i for i, n in enumerate(nums1)}
    stack = []
    for n in nums2:
        while stack and stack[-1] <= n:
            tmp = stack.pop()
            if tmp in num2idx:
                res[num2idx[tmp]] = n
        stack.append(n)
    return res

def next_greater_element2(nums1: [int], nums2: [int]) -> [int]:
    res = [0] * len(nums1)
    num2idx = {n: i for i, n in enumerate(nums1)}
    stack = []
    for i in range(len(nums2) - 1, -1, -1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()
        if nums2[i] in num2idx:
            idx = num2idx[nums2[i]]
            res[idx] = stack[-1] if stack else -1
        stack.append(nums2[i])
    return res

if __name__ == "__main__":
    res = next_greater_element([9, 7, 1], [1, 7, 9, 5, 4, 3])
    res