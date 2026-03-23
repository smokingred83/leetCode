def divide(dividend: int, divisor: int) -> int:
    if divisor == 1:
        return max(-2147483648, min(dividend, 2147483647))
    if divisor == -1:
        return max(-2147483648, min(-dividend, 2147483647))
    disor = abs(divisor)
    temp, aux, q, rem = disor, 1, 0, abs(dividend)
    while rem >= disor:
        if rem >= temp:
            q += aux
            rem -= temp
            temp += temp
            aux += aux
        else:
            temp = disor
            aux = 1
    return q if dividend ^ divisor >= 0 else -q

if __name__ == "__main__":
    res = divide(7, -3)
    res