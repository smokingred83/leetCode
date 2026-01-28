def toLowerCase(s: str) -> str:
    return "".join([_s.lower() if _s.isupper() else _s for _s in s])


if __name__ == '__main__':
    res = toLowerCase("Hello")
    res
