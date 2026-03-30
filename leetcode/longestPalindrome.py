def longestPalindrome(s: str) -> str:
    longest_l = longest_r = left = 0
    for right in range(len(s)):
        if left > 0 and s[left -1] == s[right]:
            left -= 1
        else:
            i, j = left, right
            while i < j:
                if s[i] != s[j]:
                    left += 1
                    i = left
                    j = right
                else:
                    j -= 1
                    i += 1
        if (right - left) > (longest_r - longest_l):
            longest_l = left
            longest_r = right
    return s[longest_l:longest_r+1]

def longestPalindrome1(s: str) -> str:
    result = s[0]
    for i in range(len(s)):
        left, right, delta = 0, i, 0
        while left < right:
            if s[left] == s[right]:
                delta += 1
                right -= 1
            else:
                left -= delta
                delta = 0
                right = i
            left += 1
        result = max(result, s[left - delta: i + 1], key=len)
    return result

if __name__ == "__main__":
    res = longestPalindrome("bacabab")
    res = longestPalindrome("abb")
    res = longestPalindrome("bananas")
    res = longestPalindrome("aacabdkacaa")
    res = longestPalindrome("abbcccba")
    res = longestPalindrome("aaaabaaa")
    res = longestPalindrome("cbbd")
    res