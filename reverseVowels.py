def reverseVowels(s: str) -> str:
    res = list(s)
    vows = {v for v in "a,e,i,o,u,A,E,I,O,U".split(",")}
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and res[i] not in vows:
            i += 1
        while j > i and res[j] not in vows:
            j -= 1
        res[i], res[j] = res[j], res[i]
        i += 1
        j -= 1
    return "".join(res)

if __name__ == "__main__":
    res = reverseVowels("leetcode")
    res