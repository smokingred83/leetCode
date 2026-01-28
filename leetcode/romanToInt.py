class Solution:
    _map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        if len(s) == 1:
            return Solution._map[s]

        result = 0
        for i in range(len(s) - 1):
            if Solution._map[s[i]] < Solution._map[s[i + 1]]:
                result -= Solution._map[s[i]]
            else:
                result += Solution._map[s[i]]

        result += Solution._map[s[-1]]
        return result

    def romanToInt1(self, s: str) -> int:
        result = Solution._map[s[0]]
        for i in range(1, len(s)):
            if Solution._map[s[i - 1]] < Solution._map[s[i]]:
                result -= Solution._map[s[i - 1]] * 2
            result += Solution._map[s[i]]
        return result

    def romanToInt2(s: str) -> int:
        result = 0
        for i in range(len(s)):
            if i < len(s)-1 and Solution._map[s[i]] < Solution._map[s[i+1]]:
                result -= Solution._map[s[i]]
            else:
                result += Solution._map[s[i]]
        return result

if __name__ == '__main__':
    s = Solution()
    res = s.romanToInt("MCMXCIV")
    res