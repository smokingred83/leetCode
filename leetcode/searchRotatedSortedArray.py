def search(nums: [int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while right >= left:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] >= nums[left]: # we are to the left of the rotating index
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else: # we are to the right of the rotating index
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1

if __name__ == "__main__":
    res = search([4,5,6,7,8,1,2,3], 8)
    res