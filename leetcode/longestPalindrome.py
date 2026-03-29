def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s[0]
    longest_l, longest_r, left = 0, 0, 0
    for right in range(len(s)):
        if left > 0 and s[left -1] == s[right]:
            left -= 1
        elif s[max(0, right - 2)] == s[right]:
            left = left if s[left] == s[right] else max(0, right - 2)
        else:
            left = right -1 if s[right - 1] == s[right] else right
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
    res = longestPalindrome("bacabab") # abb bananas aacabdkacaa abbcccba aaaabaaa cbbd
    res