def isAnagram(s: str, t: str) -> bool:
    for _s in s:
        if _s in t:
            c = t.count(_s)
            s = s.replace(_s, "", c)
            t = t.replace(_s, "")
    return s == t

if __name__ == '__main__':
    res = isAnagram("rat", "car")
    res