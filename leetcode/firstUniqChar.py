def firstUniqChar(s: str) -> int:
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    for k, v in counter.items():
        if v == 1:
            return s.index(k)
    return -1

if __name__ == "__main__":
    res = firstUniqChar("leetcode")
    res