class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        return max([sum(a) for a in accounts])

if __name__ == '__main__':
    s = Solution()
    res = s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
    res