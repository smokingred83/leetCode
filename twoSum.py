def twoSum(nums: list, target: int) -> list:
    diffs = {}
    nums_len = len(nums)
    for i in range(nums_len):
        index = diffs.get(target-nums[i])
        if index is None:
            diffs[nums[i]] = i
        else:
            return [index, i]

if __name__ == '__main__':
    res = twoSum([2,7,11,15], 9)
    res