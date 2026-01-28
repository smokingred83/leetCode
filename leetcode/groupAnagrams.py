class Solution:
    _abc = [*'abcdefghijklmnopqrstuvwxyz']
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        seen_strs = {}
        for s in strs:
            char_freq = [0] * len(Solution._abc)
            built_str = ""
            for c in s:
                char_freq[ord(c) - ord('a')] += 1
            for i in range(len(char_freq)):
                if char_freq[i] > 0:
                    built_str += Solution._abc[i] * char_freq[i]
            if built_str not in seen_strs:
                seen_strs[built_str] = []
            seen_strs[built_str].append(s)

        return [*seen_strs.values()]

if __name__ == '__main__':
    s = Solution()
    res = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    res