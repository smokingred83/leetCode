def permute(nums: [int]) -> [[int]]:
    result = []
    permute_recur(nums, [], result)
    return result

def permute_recur(nums: [int], acc: [int], result: []):
    if len(nums) <= 0:
        result.append(acc)
    else:
        for i in range(len(nums)):
            _acc = acc + [nums[i]]
            permute_recur(nums[:i] + nums[i + 1:], _acc, result)

if __name__ == "__main__":
    res = permute([1,2,3])
    res