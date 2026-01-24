def is_unique(s: str) -> bool:
    if len(s) > 128:
        return False
    chars_seen = [False] * 128
    for c in s:
        char = ord(c) - ord('a')
        if chars_seen[char]:
            return False
        chars_seen[char] = True
    return True


def is_unique1(s: str) -> bool:
    char_seen = set()
    for c in s:
        if c in char_seen:
            return False
        char_seen.add(c)
    return True

if __name__ == "__main__":
    res = is_unique("abcd")
    res