def hammingWeight(n: int) -> int:
    res = 0
    for _ in range(len(bin(n)[2:])):
        res += n & 1
        n = n >> 1
    return res

def hammingWeight_1(n: int) -> int:
    res = 0
    while n > 0:
        res += n & 1
        n = n >> 1
    return res

if __name__ == "__main__":
    res = hammingWeight(11)
    res