def sortColors(nums: [int]) -> None:
    arr = [n for n in nums]
    idx_0, idx_2, ones = 0, len(nums) - 1, 0
    for i in range(len(nums)):
        if arr[i] == 0:
            nums[idx_0] = 0
            idx_0 += 1
        elif arr[i] == 2:
            nums[idx_2] = 2
            idx_2 -= 1
        else:
            ones += 1
    while ones > 0:
        nums[idx_0] = 1
        idx_0 += 1
        ones -= 1


if __name__ == "__main__":
    nums = [2,0,1]
    res = sortColors(nums)
    res