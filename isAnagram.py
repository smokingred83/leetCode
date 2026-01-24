class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_freq = {}
        for i in range(len(s)):
            char_freq[s[i]] = char_freq.get(s[i], 0) + 1
            char_freq[t[i]] = char_freq.get(t[i], 0) - 1
        return not any(char_freq.values())

    def isAnagram1(s: str, t: str) -> bool:
        for _s in s:
            if _s in t:
                c = t.count(_s)
                s = s.replace(_s, "", c)
                t = t.replace(_s, "")
        return s == t

if __name__ == '__main__':
    s = Solution()
    res = s.isAnagram("rat", "car")
    res