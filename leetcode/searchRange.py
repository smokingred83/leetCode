def searchRange(nums: [int], target: int) -> [int]:
    if len(nums) <= 0:
        return [-1, -1]

    l, r = 0, len(nums) - 1
    while r >= l:
        m = (r + l) // 2
        if nums[m] == target:
            s, e = m, m
            while s >= 0 and nums[s] == target:
                s -= 1
            while e < len(nums) and nums[e] == target:
                e += 1
            return [s + 1, e - 1]
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return [-1, -1]

if __name__ == "__main__":
    res = searchRange([2, 2], 3)
    res