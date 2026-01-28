def mySqrt(x: int) -> int:
    if x <= 1:
        return x
    res = left = 1
    right = x // 2
    while left <= right:
        middle = (right + left) // 2
        power = middle ** 2
        if power == x:
            return middle
        if power < x:
            res = left
            left = middle + 1
        else:
            res = right = middle -1
    return res

def mySqrt1(x: int) -> int:
    if x <= 1:
        return x
    res = x // 2
    while res ** 2 > x:
        res //= 2
    while x // res >= res:
        res += 1
    return res - 1

if __name__ == "__main__":
    res = mySqrt(15)
    res