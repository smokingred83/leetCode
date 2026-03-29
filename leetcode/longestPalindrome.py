def longestPalindrome(s: str) -> str:
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
    res = longestPalindrome("aaaabaaa") # abbcccba
    res