def repeatedSubstringPattern(s: str) -> bool:
    len_s = len(s)
    seq = ''
    for i in range(len_s // 2):
        seq += s[i]
        if (len(seq) * s.count(seq)) == len_s:
            return True
    return False


def repeatedSubstringPattern_goodSolution(s: str) -> bool:
    return (s * 2)[1:-1].find(s) != -1


if __name__ == '__main__':
    res = repeatedSubstringPattern("a")
    res = repeatedSubstringPattern_goodSolution("a")
    res