class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        pre, post = [1] * len(nums), [1] * len(nums)
        i, j = 1, len(nums) - 2
        while i < len(nums) and j >= 0:
            pre[i] = pre[i - 1] * nums[i -1]
            post[j] = post[j + 1] * nums[j + 1]
            i += 1
            j -= 1
        return [pre[i] * post[i] for i in range(len(pre))]

    def productExceptSelf1(self, nums: [int]) -> [int]:
        answers = [1] * len(nums)
        pre, post = 1, 1
        for i in range(1, len(nums)):
            pre *= nums[i - 1]
            answers[i] = pre
        for i in range(len(nums) - 2, -1, -1):
            post *= nums[i + 1]
            answers[i] *= post
        return answers

if __name__ == '__main__':
    s = Solution()
    res = s.productExceptSelf([1,2,3,4])
    res