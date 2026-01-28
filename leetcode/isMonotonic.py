def isMonotonic(nums: [int]) -> bool:
    isIncreasing = False
    idx = len(nums)
    for i in range(0, len(nums) - 1):
        if nums[i] is not nums[i + 1]:
            isIncreasing = nums[i] < nums[i + 1]
            idx = i + 1
            break;
    if isIncreasing:
        return all(nums[i] <= nums[i+1] for i in range(idx, len(nums)-1))
    return all(nums[i] >= nums[i + 1] for i in range(idx, len(nums) - 1))

if __name__ == '__main__':
    res = isMonotonic([1,2,2,3])
    res