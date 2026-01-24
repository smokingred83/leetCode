class Solution:
    def __init__(self):
        self.mapping = {c:i for i, c in enumerate("0123456789")}

    def multiply(self, num1: str, num2: str) -> str:
        def get_sum(num):
            l = len(num) - 1
            res = 0
            i = 0
            while i < l:
                res += self.mapping[num[i]] * 10 ** (l - i)
                i += 1
            return res + self.mapping[num[l]]
        return str(get_sum(num1) * get_sum(num2))

if __name__ == '__main__':
    s = Solution()
    res = s.multiply(num1='10', num2='15')
    res