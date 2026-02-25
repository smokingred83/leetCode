def length_of_Longest_Substring(s: str) -> int:
    start, longest = 0, 0
    chars_seen = set()
    for end, char in enumerate(s):
        if char in chars_seen:
            longest = max(longest, end - start)
            while True:
                chars_seen.remove(s[start])
                if s[start] == char:
                    start += 1
                    break
                start += 1
        chars_seen.add(char)
    return max(longest, len(s) - start)


def length_of_Longest_Substring2(s: str) -> int:
    i, tmp, longest = 0, 0, 0
    while len(s) - longest > i:
        chars_seen = set()
        j, tmp = i, 0
        while j < len(s) and s[j] not in chars_seen:
            chars_seen.add(s[j])
            j += 1
            tmp += 1
        longest = max(longest, tmp)
        i += 1
    return max(longest, tmp)

if __name__ == "__main__":
    res = length_of_Longest_Substring("abccbad")
    res