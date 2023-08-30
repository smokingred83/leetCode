def maxSubArray(nums: [int]) -> int:
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
    res1 = maxSubArray(input)
    res2 = maxSubArray_divideConquer(input)
    res1 == res2