def sortedSquares(nums: [int]) -> [int]:
    n = len(nums)
    squares = [0 for _ in range(n)]
    l, r = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[l]) >= abs(nums[r]):
            squares[i] = nums[l] ** 2
            l += 1
        else:
            squares[i] = nums[r] ** 2
            r -= 1
    return squares

if __name__ == "__main__":
    res = sortedSquares([-4,-1,0,3,10])
    res