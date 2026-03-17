def lengthOfLIS(nums: [int]) -> int:
    result = []
    for i in range(len(nums)):
        pos = search(result, nums[i])
        if pos >= len(result):
            result.append(nums[i])
        else:
            result[pos] = nums[i]
    return len(result)

def search(nums: [int], tgt: int) -> int:
    left, right = 0, len(nums) -1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == tgt:
            return middle
        if nums[middle] < tgt:
            left = middle + 1
        elif nums[middle] > tgt:
            right = middle -1
    return left

def lengthOfLIS_cuadratic(nums: [int]) -> int:
    result = []
    for i in range(len(nums)):
        prev = 0
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                prev = max(prev, result[j])
        result.append(1 + prev)
    return max(result)

if __name__ == "__main__":
    res = lengthOfLIS([4,10,4,3,8,9])
    res = lengthOfLIS([10,9,2,5,3,7,101,18])
    res = lengthOfLIS([0,1,0,3,2,3])
    res = lengthOfLIS([7,7,7,7,7,7,7])
    res = lengthOfLIS([1,3,2])
    res