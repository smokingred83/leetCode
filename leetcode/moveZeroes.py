def moveZeroes(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    temp_idx = 0
    for i in range(len(nums)):
        if nums[temp_idx] == 0:
            nums.append(nums.pop(temp_idx))
        else:
            temp_idx += 1

if __name__ == '__main__':
    res = moveZeroes([0,0,1])
    res