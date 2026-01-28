import math


def countOdds(low: int, high: int) -> int:
    result = (high - low) // 2
    if low & 1 == 1 or high & 1 == 1:
        return result + 1
    return result

if __name__ == '__main__':
    res = countOdds(14, 17)
    res