from typing import List


def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    res = singleNumber([2, 2, 1])
    res