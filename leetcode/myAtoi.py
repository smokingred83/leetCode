def myAtoi(s: str) -> int:
    if len(s) <= 0 or all([c == " " for c in s]):
        return 0
    start, is_negative = 0, False

    while s[start] == " ":
        start += 1
    if s[start] == "-":
        is_negative = True
        start += 1
    elif s[start] == "+":
        start += 1

    end = start
    while end < len(s) and 48 <= ord(s[end]) <= 57:
        end += 1

    result = int(s[start:end]) if end - start > 0 else 0
    return max(-result, -2 ** 31) if is_negative else min(result, 2 ** 31 - 1)

def myAtoi_1(s: str) -> int:
    result = 0
    if len(s) <= 0 or all([c == " " for c in s]):
        return result
    start, is_negative = 0, False

    while s[start] == " ":
        start += 1
    if s[start] == "-":
        is_negative = True
        start += 1
    elif s[start] == "+":
        start += 1

    end = start
    while end < len(s) and 48 <= ord(s[end]) <= 57:
        end += 1

    length = end - start
    for i, power in zip(range(start, end), range(length - 1, -1, -1)):
        result += 10 ** power * int(s[i])

    if is_negative:
        return max(-result, -2 ** 31)
    return min(result, 2 ** 31 - 1)

if __name__ == "__main__":
    res = myAtoi("-42")
    res