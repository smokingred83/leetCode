def strStr(haystack: str, needle: str) -> int:
    i = 0
    while i <= len(haystack) - len(needle):
        if haystack[i] == needle[0]:
            found = True
            for j in range(1, len(needle)):
                if haystack[i + j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        i += 1
    return -1

if __name__ == '__main__':
    res = strStr("leetcode", "leeto")
    res