def maxSubArray(nums: [int]) -> int:
    _max = current = nums[0]
    for i in range(1, len(nums)):
        current = max(current + nums[i], nums[i])
        _max = max(_max, current)
    return _max

def maxSubArray_old(nums: [int]) -> int:
    current = result = nums[0]
    for i in range(1, len(nums)):
        temp = current + nums[i]
        if nums[i] > temp:
            current = nums[i]
        else:
            current = temp
        if current > result:
            result = current
    return result

def maxSubArray_divideConquer(nums: [int]) -> int:
    current = result = nums[0]
    for i in range(1, len(nums)):
        current += nums[i]
        if nums[i] > current:
            return max(result, maxSubArray_divideConquer(nums[i:]))
        if current > result:
            result = current
    return result

if __name__ == '__main__':
    input = [-2,1,-3,4,-1,2,1,-5,4]
    res1 = maxSubArray_old(input)
    res2 = maxSubArray_divideConquer(input)
    res1 == res2
    assert maxSubArray([1, -2, 0]) == 1
    assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5, 4, -1, 7, 8]) == 23
    assert maxSubArray([1, 2]) == 3
    assert maxSubArray([-1, -2]) == -1
    assert maxSubArray([8, -19, 5, -4, 20]) == 21