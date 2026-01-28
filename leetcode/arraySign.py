def arraySign(nums: [int]) -> int:
    mid = len(nums) // 2
    res = 1
    for i in range(mid):
        res *= nums[i] * nums[-1-i]
    if len(nums) % 2 != 0:
        res *= nums[mid]
    return 1 if res >= 1 else max(-1, res)

if __name__ == '__main__':
    res = arraySign([-5])
    res