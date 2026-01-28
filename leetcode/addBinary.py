def addBinary(a: str, b: str) -> str:
    return bin(int(a, base=2) + int(b, base=2))[2:]


def addBinary2(a: str, b: str) -> str:
    if a == '0' and b == '0':
        return a
    a_length, b_length = len(a), len(b)
    num1 = sum([2 ** (a_length - i - 1) for i in range(a_length - 1) if a[i] == '1'])
    num1 += int(a[-1])
    num2 = sum([2 ** (b_length - i - 1) for i in range(b_length - 1) if b[i] == '1'])
    num2 += int(b[-1])
    return bin(num1 + num2).lstrip('0b')


if __name__ == '__main__':
    res = addBinary("0", "0")
    res
