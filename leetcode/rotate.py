from typing import List


def rotate(nums: List[int], k: int) -> None:
    pivot = len(nums) - (k % len(nums))
    reverse(nums, 0, pivot)
    reverse(nums, pivot, len(nums))
    reverse(nums, 0, len(nums))

def reverse(nums: List[int], start: int, end: int):
    front = start
    back = end - 1
    for i in range((end - start) // 2):
        tmp = nums[front + i]
        nums[front + i] = nums[back - i]
        nums[back - i] = tmp

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    rotate(nums, 10)
    print("")