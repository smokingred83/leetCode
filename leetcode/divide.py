def divide(dividend: int, divisor: int) -> int:
    if divisor == 1:
        return dividend
    if divisor == -1:
        return -dividend
    dend, disor = abs(dividend), abs(divisor)
    quotient = 0
    while dend >= disor:
        dend -= disor
        quotient += 1
    return quotient if dividend ^ divisor >= 0 else -quotient

if __name__ == "__main__":
    res = divide(-1, 1)
    res