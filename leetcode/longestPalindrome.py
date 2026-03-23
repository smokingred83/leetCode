def longestPalindrome(s: str) -> str:
    result, temp = "", ""
    for i in range(len(s) - 1):
        left = i
        if len(result) >= len(s) - i:
            break
        for right in range(len(s) -1, i, -1):
            middle = (right + left) // 2
            while left >= middle:
                if s[left] == s[right]:
                    temp += s[left]
                    left += 1
                else:
                    temp = ""
                    left = i
        result = max(result, temp, key=len)
        temp = ""
    return result

if __name__ == "__main__":
    res = longestPalindrome("babad")
    res