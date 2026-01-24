class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen_nums = set()
        for i in range(len(nums)):
            if nums[i] in seen_nums:
                return True
            seen_nums.add(nums[i])
            if len(seen_nums) > k:
                seen_nums.remove(nums[i - k])
        return False

    def containsNearbyDuplicate2(self, nums: list[int], k: int) -> bool:
        window, seen_nums = [], set()
        left, right = 0, 0
        while right < len(nums):
            window.append(nums[right])
            seen_nums.add(nums[right])
            if len(seen_nums) < len(window):
                return True
            if (right - left) >= k:
                val = window.pop(0)
                seen_nums.remove(val)
                left += 1
            right += 1
        return False

    def containsNearbyDuplicate1(self, nums: list[int], k: int) -> bool:
        seen_nums = {}
        for i in range(len(nums)):
            if nums[i] in seen_nums and abs(i - seen_nums.get(nums[i])) <= k:
                return True
            seen_nums[nums[i]] = i
        return False

if __name__ == '__main__':
    s = Solution()
    res = s.containsNearbyDuplicate([1,0,1,1], 1)
    res