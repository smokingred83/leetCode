from math import sqrt


def countPrimes(n: int) -> int:
    if n <= 1:
        return 0
    primes = [True for _ in range(n)]
    primes[0] = False
    primes[1] = False
    for idx in range(2, int(sqrt(n)) + 1):
        if primes[idx]:
            for multiple in range(idx ** 2, n, idx):
                primes[multiple] = False
    return sum(primes)


if __name__ == "__main__":
    res = countPrimes(10)
    res