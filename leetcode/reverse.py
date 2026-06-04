def reverse_recur_1(x: int, power: int) -> int:
    if power < 0:
        return 0
    tmp = x
    if x < 0:
        tmp *= -1
    rem = tmp % 10
    tmp //= 10
    res = reverse_recur_1(tmp * -1 if x < 0 else tmp, power -1)
    rem = rem * -1 if x < 0 else rem
    return res + rem * 10 ** power

def reverse_1(x: int) -> int:
    power = len(str(x)) - 1
    if x < 0:
        power -= 1
    res = reverse_recur_1(x, power)
    return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0

def reverse_2(x: int) -> int:
    digits, is_neg, temp = str(x), False, x
    if x < 0:
        digits = digits[1:]
        temp *= -1
        is_neg = True

    res = 0
    for i in range(len(digits)):
        res += int(digits[i]) * 10 ** i

    res = res * -1 if is_neg else res
    return res if -2 ** 31 <= res <= 2 ** 31 -1 else 0

def reverse_recur(x: int, rev: int) -> int:
    if x == 0:
        return rev
    tmp = x
    if x < 0:
        tmp *= -1
    rem = tmp % 10
    tmp //= 10
    rem = rem * -1 if x < 0 else rem
    rev = rev * 10 + rem
    return reverse_recur(tmp * -1 if x < 0 else tmp, rev)

def reverse(x: int) -> int:
    res = reverse_recur(x, 0)
    return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0

if __name__ == "__main__":
    res = reverse(-123)
    res