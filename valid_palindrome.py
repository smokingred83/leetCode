def isPalindrome(s: [str]) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and not in_range(s, i):
            i += 1
        while j > i and not in_range(s, j):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def in_range(s, i):
    return 0 <= ord(s[i].lower()) - ord('a') < 26\
                or 48 <= ord(s[i].lower()) <= 57


if __name__ == "__main__":
    res = isPalindrome("0P")
    res