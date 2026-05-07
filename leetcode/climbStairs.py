def climbStairs(n: int) -> int:
    memo = {}
    return climbStairs_memo(n, memo)

def climbStairs_memo(n: int, memo: dict):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = climbStairs_memo(n - 1, memo) + climbStairs_memo(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    res = climbStairs(3)
    res