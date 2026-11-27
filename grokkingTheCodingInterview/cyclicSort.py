def sort(nums: [int]) -> [int]:
    i = 0
    while i < len(nums):
        home = nums[i] - 1
        if home != i:
            nums[i], nums[home] = nums[home], nums[i]
        else:
            i = i + 1
    return nums

if __name__ == "__main__":
    nums = [3, 1, 5, 4, 2]
    res = sort(nums)
    res