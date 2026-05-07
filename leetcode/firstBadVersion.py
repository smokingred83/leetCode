def isBadVersion(n: int) -> int:
    if n == 1 or n == 2 or n == 3:
        return False
    return True

def firstBadVersion(n: int) -> int:
    left = 1
    right = n
    while right > left:
        m = (right + left) // 2
        if isBadVersion(m):
            right = m
        else:
            left = m + 1
    return left


if __name__ == "__main__":
    res = firstBadVersion(5)
    res