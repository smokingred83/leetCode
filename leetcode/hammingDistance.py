def hammingDistance(x: int, y: int) -> int:
    dis = x ^ y
    res = 0
    while dis > 0:
        res += dis & 1
        dis = dis >> 1
    return res

def hammingDistance_1(self, x: int, y: int) -> int:
    res = 0
    while x ^ y > 0:
        res += (x ^ y) & 1
        x = x >> 1
        y = y >> 1
    return res

if __name__ == "__main__":
    res = hammingDistance(1, 3)
    res