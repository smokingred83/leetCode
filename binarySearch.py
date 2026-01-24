class Solution:
    def search(self, nums: [int], target: int) -> int:
        left, right = 0, (len(nums) - 1)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    res = s.search([-1,0,3,5,9,12], 13)
    res