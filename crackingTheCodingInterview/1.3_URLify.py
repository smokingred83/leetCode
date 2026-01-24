def urlify(s: str, l: int) -> str:
    res = list(s)
    space_count = 0
    for i in range(l):
        if res[i] == " ":
            space_count += 1
    shift = space_count * 2
    for i in range(l - 1, -1, -1):
        if res[i] == " ":
            res[i + shift] = "0"
            res[i + shift - 1] = "2"
            res[i + shift - 2] = "%"
            shift -= 2
        else:
            res[i + shift] = res[i]
    return "".join(res)

if __name__ == "__main__":
    s = "Mr John Smith    "
    res = urlify(s, 13)
    res