class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(nums[i] + result[i - 1])
        return result

if __name__ == '__main__':
    s = Solution()
    res = s.runningSum([1,2,3,4])
    res