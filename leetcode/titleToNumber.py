def titleToNumber(columnTitle: str) -> int:
    l = len(columnTitle)
    result = 0
    for i, p in zip(range(l), range(l -1, -1, -1)):
        result += (ord(columnTitle[i]) - 64) * 26 ** p
    return result

if __name__ == "__main__":
    res = titleToNumber("ZY")
    res